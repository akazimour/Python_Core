import time
from typing import Dict


execution_time: Dict[str, float] = {}


def time_decorator(func):
    from time import time
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        end = time() - t1
        execution_time[func.__name__] = end
        return result

    return wrapper

@time_decorator
def func_add(a, b):
    time.sleep(0.2)
    return a + b

print(func_add(10, 20))
print(execution_time['func_add'])

