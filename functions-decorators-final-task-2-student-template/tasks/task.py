from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    c = 0
    g = 0
    ret_array = []
    container_str = ''
    while c < len(indexes):
        while g < len(s):
            if g == indexes[c]:
                ret_array.append(container_str)
                container_str = ''
                container_str += s[g]
                g += 1
                if c < len(indexes) - 1:
                    c += 1
            else:
                container_str += s[g]
                g += 1
        c += 1
    ret_array.append(container_str)
    return ret_array


