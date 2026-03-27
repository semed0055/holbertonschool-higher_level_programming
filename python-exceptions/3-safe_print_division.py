#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result in the finally section."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
