from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    collection_list = []
    for i in lst:
        keys = i.keys()
        for j in keys:
            collection_list.append(i.get(j))
    return set(collection_list)

