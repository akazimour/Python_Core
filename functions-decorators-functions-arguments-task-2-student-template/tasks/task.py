from functools import reduce


def union(*args) -> set:
    return_list = []
    output = list(map(lambda x: return_list.append(list(x)), args))
    return_set = set(sum(return_list, []))
    return return_set


def intersect(*args) -> set:
    common_elements = reduce(lambda z, t: set(z) & set(t), args)
    return common_elements
