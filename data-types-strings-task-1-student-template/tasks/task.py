def get_fractions(a_b: str, c_b: str) -> str:
    first_part = a_b.split('/')
    second_part = c_b.split('/')
    first = int(first_part[0])
    second = int(second_part[0])
    down = first_part[1]
    summary = first + second
    sum_string = str(summary)
    return a_b + ' + ' + c_b + ' = ' + sum_string + '/' + down

