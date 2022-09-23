#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char_c in my_string:
        if char_c != 'c' and char_c != 'C':
            new_string += char_c
    return new_string
