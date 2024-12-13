from typing import List
from functools import reduce
from operator import mul

def foo(nums: List[int]) -> List[int]:
    counter = 0
    final_list_to_return = []
    for j in range(len(nums)):
        created_list = []
        for i in range(len(nums)):
            if i == counter:
                continue
            created_list.append(nums[i])
        final_list_to_return.append(reduce(mul, created_list))
        counter += 1
    return final_list_to_return

