from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    return_number = []
    for elem in sequence:
        if isinstance(elem, list) or isinstance(elem, tuple):
            return_number.extend(linear_seq(elem))
        else:
            return_number.append(elem)
    return return_number
