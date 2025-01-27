
def validate(func):
    def wrapper(*args):
        for i in args:
            if i<0 or i>256:
              return "Function call is not valid!"
        return func(*args)

    return wrapper



@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"

print(set_pixel(0, 127, 300))
print(set_pixel(0,127,250))