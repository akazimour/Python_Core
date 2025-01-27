import time

def log(func):
    def wrapper(*args,**kwargs):
        f_path = 'log.txt'
        start_time = time.time()
        res=func(*args, **kwargs)
        end_time= time.time()
        exec_time=end_time-start_time

        first_str = ", ".join(f"{k}={v}" for k,v in zip(func.__code__.co_varnames,args))
        second_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        with open(f_path,'w')as file:
            file.write(f'{func.__name__}; args: {first_str}; kwargs: {second_str}; execution time: {exec_time} sec.')
        return res
    return wrapper


@log
def foo(a, b, c=3):
    return a+b+c

print(foo(1,2,c=3))




