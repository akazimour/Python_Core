from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    dictionary={}
    for i in s:
        lower = i.lower()
        if lower in dictionary:
            dictionary[lower]+=1
        else:
            dictionary[lower]=1
    return dictionary

print(get_dict('Oh, it is python'))