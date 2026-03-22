#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Açarları əlifba sırası ilə sıralayırıq
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
