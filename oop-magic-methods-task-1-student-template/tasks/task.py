from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values


    def __add__(self, b):
        ret_arr=[]
        for v in self.values:
            ret_arr.append(str(v)+" "+b)
        return ret_arr
