from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    converted_set = set(str_list)
    set_to_list = list(converted_set)
    set_to_list=sorted(set_to_list)
    return set_to_list
