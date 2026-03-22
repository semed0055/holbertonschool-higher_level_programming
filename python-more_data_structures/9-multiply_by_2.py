#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Dictionary comprehension istifadə edərək yeni lüğət yaradırıq
    return {key: value * 2 for key, value in a_dictionary.items()}
