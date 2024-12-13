from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    some_list = []
    for x in range(1, n+1):
        if not x % 3 and not x % 5:
            some_list.append("FizzBuzz")
        elif not x % 3:
            some_list.append("Fizz")
        elif not x % 5:
            some_list.append("Buzz")
        else:
            some_list.append(x)
    return some_list

