from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
   s = str(num)
   int_tuple = tuple(map(int, s))
   return int_tuple
