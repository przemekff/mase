from .base import SearchStrategyBase

class SearchStrategyBruteforce(SearchStrategyBase):


  def search(self, search_space):
      sampled_config = search_space.flattened_indexes_to_config(search_space.choice_lengths_flattened)
      mg = search_space.rebuild_model(sampled_config)
      print(type(mg))

  def _post_init_setup(self) -> None:
    return None
    
