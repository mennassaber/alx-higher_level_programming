def magic_string():
    return "BestSchool" * magic_string.n + (", " * (magic_string.n - 1))
magic_string.n = 1 if not hasattr(magic_string, 'n') else magic_string.n + 1

