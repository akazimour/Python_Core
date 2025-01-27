from typing import Dict

l = {'a': 100, 'b': 200}
l2= {'a': 200, 'c': 300}
l3 ={'a': 300, 'd': 100}

def combine_dicts(*args:Dict[str, int]) -> Dict[str, int]:
    dict_to_return = {}
    dict_items = [d for d in args]
    for d in dict_items:
        for k, v in d.items():
            if k in dict_to_return:
                dict_to_return[k] = dict_to_return.get(k) + v
            else:
                dict_to_return[k] = v
    return dict_to_return

print(combine_dicts(l2,l3))