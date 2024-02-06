from .base import SearchStrategyBase

def generate_combinations(original, current_index=0, current_combination=[]):

    if current_index == len(original):
        return [current_combination]
    

    combinations = []
    for i in range(original[current_index] + 1):
        combinations += generate_combinations(original, current_index + 1, current_combination + [i])
    
    return combinations

class SearchStrategyBruteforce(SearchStrategyBase):






  def search(self, search_space):
    sampled_indexes = {}
    
    #print(search_space)
    indexes = list(search_space.choice_lengths_flattened.values())
    indexes = [x - 1 for x in indexes]
    print(indexes)

    sampled_config = search_space.flattened_indexes_to_config(sampled_indexes)
    
    lists = generate_combinations(indexes)

    
    for sublist in lists:
      #print(sublist)
      i = 0
      for name, length in search_space.choice_lengths_flattened.items():
        sampled_indexes[name] = sublist[i]
        i = i+1
      print(sampled_indexes)
    



  def _post_init_setup(self) -> None:
    return None
    
