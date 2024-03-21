#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    total = 0
    prev_value = 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for r in reversed(roman_string):
        value = digits.get(r)
        if value is None:
            return 0  # Invalid Roman numeral encountered
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total
