from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    l = list(zip(lst[0::], lst[1::]))
    return l

