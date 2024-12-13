def get_longest_word( s: str) -> str:
    longest = ''
    sliced = s.split()
    for x in sliced:
        if len(x) > len(longest):
            longest = x
    return longest

