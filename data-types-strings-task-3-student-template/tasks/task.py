def replacer(s: str) -> str:
    replaced = s.maketrans({'"': "'", "'": '"'})
    s = s.translate(replaced)
    return s



