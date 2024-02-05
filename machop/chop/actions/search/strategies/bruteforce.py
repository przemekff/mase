from .base import SearchStrategyBase

class SearchStrategyBruteforce(SearchStrategyBase):


  def search(self, search_space):
      #sampled_config = search_space.flattened_indexes_to_config(search_space.choice_lengths_flattened)
      #print(search_space.choice_lengths_flattened)
      #print(type(search_space.choice_lengths_flattened))
      #mg = search_space.rebuild_model(sample)
      #print(type(mg))
      sampled_indexes = {}
      #for name, length in search_space.choice_lengths_flattened.items():
        #print(name)
        #sampled_indexes[name] = 
      sampled_config = search_space.flattened_indexes_to_config(sampled_indexes)
      mg = search_space.rebuild_model(sampled_config)


  def _post_init_setup(self) -> None:
    return None
    
