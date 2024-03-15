#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Fill missing elements with 0 and take only the first 2 elements
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    # Return a tuple containing the sum of corresponding elements
    return (a[0] + b[0], a[1] + b[1])
if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)
    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
