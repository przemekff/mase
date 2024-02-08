from .base import SearchStrategyBase

import torch

def generate_combinations(original, current_index=0, current_combination=[]):

    if current_index == len(original):
        return [current_combination]
    

    combinations = []
    for i in range(original[current_index] + 1):
        combinations += generate_combinations(original, current_index + 1, current_combination + [i])
    
    return combinations

class SearchStrategyBruteforce(SearchStrategyBase):



  def compute_software_metrics(self, model, sampled_config: dict, is_eval_mode: bool):
    # note that model can be mase_graph or nn.Module
    metrics = {}
    if is_eval_mode:
        with torch.no_grad():
            for runner in self.sw_runner:
                metrics |= runner(self.data_module, model, sampled_config)
    else:
        for runner in self.sw_runner:
            metrics |= runner(self.data_module, model, sampled_config)
    return metrics

  def compute_hardware_metrics(self, model, sampled_config, is_eval_mode: bool):
      metrics = {}
      if is_eval_mode:
          with torch.no_grad():
              for runner in self.hw_runner:
                  metrics |= runner(self.data_module, model, sampled_config)
      else:
          for runner in self.hw_runner:
              metrics |= runner(self.data_module, model, sampled_config)
      return metrics


  def search(self, search_space):
    sampled_indexes = {}
    is_eval_mode = self.config.get("eval_mode", True)
    
    #print(search_space)
    indexes = list(search_space.choice_lengths_flattened.values())
    indexes = [x - 1 for x in indexes]
    print(indexes)

    
    
    lists = generate_combinations(indexes)

    
    for sublist in lists:
      #print(sublist)
      i = 0
      for name, length in search_space.choice_lengths_flattened.items():
        sampled_indexes[name] = sublist[i]
        i = i+1
      sampled_config = search_space.flattened_indexes_to_config(sampled_indexes)
      print(sampled_config)
      model = search_space.rebuild_model(sampled_config)
      software_metrics = self.compute_software_metrics(
            model, sampled_config, is_eval_mode
        )
      hardware_metrics = self.compute_hardware_metrics(
            model, sampled_config, is_eval_mode
        )

      print(software_metrics)
      print(hardware_metrics)
    



  def _post_init_setup(self) -> None:
    return None
    
