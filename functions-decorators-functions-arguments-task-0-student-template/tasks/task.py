from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    dictionary = {}
    for i in range(1, num + 1):
        dictionary[i] = i * i
    return dictionary



