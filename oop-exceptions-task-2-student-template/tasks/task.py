from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    split_str = str_with_ints.split()
    output_str = ' '.join(split_str)
    chr_arr = output_str.split(' ')
    int_container = []
    for c in chr_arr:
        try:
           int_c = int(c)
           int_container.append(int_c)
        except (ValueError,TypeError) as e:
            return f'Error code: {e}'
    try:
        float_num = int_container[0] / int_container[1]
    except ZeroDivisionError as err:
        return f'Error code: {err}'
    else:
        return float_num
