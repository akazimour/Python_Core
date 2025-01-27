
def decorator_apply(lambda_func):
    def decorator(func):
        def wrapper(*args,**kwargs):
            return lambda_func(func(*args,**kwargs))
        return wrapper
    return decorator



@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num

print(return_user_id(42) )
