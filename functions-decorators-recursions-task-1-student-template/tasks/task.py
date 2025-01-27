from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]):
    return_number=[]
    for elem in sequence:
        if isinstance(elem,list) or isinstance(elem,tuple) :
            return_number.extend(seq_sum(elem))
        else:
            return_number.append(elem)
    return return_number
squ = [1,2,3,[4,5, (6,7)]]
print(seq_sum(squ))