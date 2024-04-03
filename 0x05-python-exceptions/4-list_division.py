#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print('Division by 0 at index', i)
            result = 0
        except IndexError:
            print('Index out of range at index', i)
            result = 0
        except TypeError:
            print('Wrong type at index', i)
            result = 0
        finally:
            new_list.append(result)
    return new_list
