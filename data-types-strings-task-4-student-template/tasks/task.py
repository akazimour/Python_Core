def check_str(s: str):
    character: str = ''
    for ch in s:
        if ch.isalpha() or ch.isdigit():
            character += ch
    character = character.lower()
    if character == character[::-1]:
        return True
    return False
