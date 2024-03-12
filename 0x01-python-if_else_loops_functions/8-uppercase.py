#!/usr/bin/python3
def uppercase(s):
"""Prints a string in uppercase followed by a new line."""
for char in s:
if 'a' <= char <= 'z':  # Check if the character is lowercase
print(chr(ord(char) - 32), end='')  # Convert to uppercase using ASCII values
else:
print(char, end='')
print()  # Print a new line after printing the uppercase string
# Test cases
uppercase("best")
uppercase("Best School 98 Battery street")

