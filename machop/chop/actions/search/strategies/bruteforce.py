from .base import SearchStrategyBase

class SearchStrategyBruteforce(SearchStrategyBase):


  def search(self, search_space):
    sampled_indexes = {}
    #add a loop to traverse through the whole search space
    print(search_space)
    for name, length in search_space.choice_lengths_flattened.items():
      print(length)
      sampled_indexes[name] = 0
    sampled_config = search_space.flattened_indexes_to_config(sampled_indexes)



  def _post_init_setup(self) -> None:
    return None
    
