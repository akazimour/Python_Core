from typing import List
import re

def split(data: str, sep=None, maxsplit=-1):
    ret_array = []
    container_str = ''
    counter = 0
    len1 = len(data)
    sep_length=0
    if sep is not None:
        sep_length = len(sep)


    if len(data) == 0 or data.isspace() and sep is None and maxsplit == -1:
        return ret_array
    elif len(data) != 0 and sep is None and maxsplit == 0:
        data = data.strip()
        ret_array.append(data)
        return ret_array
    elif len(data) != 0 and sep_length>0 and data.find(sep)==-1 and maxsplit == -1:
        ret_array.append(data[::])
        return ret_array
    elif len(data) != 0 and sep is None and maxsplit == -1:
        data = data.strip()
        data = re.sub(' +', ' ', data)
        for c in data:
            if c == " ":
                ret_array.append(container_str)
                container_str = ''
            else:
                container_str += c
        ret_array.append(container_str)
        return ret_array
    elif len(data) != 0 and sep is None and maxsplit > 0:
        data = data.strip()
        for ch in range(len(data)):
            if data[ch] != " ":
                container_str = container_str.strip()
                container_str += data[ch]
            elif data[ch] == " " and len(container_str) > 0 and maxsplit > len(ret_array):
                ret_array.append(container_str)
                container_str = ''
            elif data[ch] == " " and len(container_str) <= 0 and maxsplit > len(ret_array):
                continue
            elif maxsplit <= len(ret_array):
                container_str += data[ch::]
                container_str = container_str.strip()
                ret_array.append(container_str)
                return ret_array
    elif sep_length == 1:
        for c in range(len(data)):
            if len(ret_array) >= maxsplit > 0:
                container_str += data[c::]
                ret_array.append(container_str)
                return ret_array
            elif c == len(data) - 1 and data[c] == sep:
                ret_array.append(container_str)
                ret_array.append('')
                container_str = ''
            elif data[c] == sep:
                ret_array.append(container_str)
                container_str = ''
            else:
                container_str += data[c]

        return ret_array
    elif sep_length > 1:
        if maxsplit == 0:
            ret_array.append(data)
            return ret_array
        elif maxsplit < 0:
            return calc_last_test_case(container_str, counter, data, len1, ret_array, sep, sep_length,maxsplit)
        elif maxsplit>0:
            return calc_last_test_case(container_str, counter, data, len1, ret_array, sep, sep_length,maxsplit)


def calc_last_test_case(container_str, counter, data, len1, ret_array, sep, sep_length,maxsplit):
    ending_of_test_word = data[len1 - sep_length]
    while sep == ending_of_test_word[::]:
        data = data[:len(data) - sep_length]
        ending_of_test_word = data[len(data) - sep_length]
        counter += 1
    len1 = len(data)
    res = [i for i in range(len(data)) if data.startswith(sep, i)]
    res_length = len(res)
    length = res_length
    final_length = len1 - sep_length * length
    c = 0
    g = 0
    while c < len(res):
        while g < len(data):
            if g == res[c]:
                if len(ret_array)>=maxsplit:
                    container_str+=data[g::]
                    ret_array.append(container_str)
                    return ret_array
                ret_array.append(container_str)
                g = g + sep_length
                container_str = ''
                if c < len(res) - 1:
                    c += 1
            else:
                container_str += data[g]
                g += 1
        c += 1
    ret_array.append(container_str)
    if counter > 0:
        for i in range(counter):
            ret_array.append('')
    return ret_array


if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']

print(split(' '))



