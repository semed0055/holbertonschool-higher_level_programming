#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # pop(key, None) açar varsa silir, yoxdursa heç nə etmir (xəta vermir)
    a_dictionary.pop(key, None)
    return a_dictionary
