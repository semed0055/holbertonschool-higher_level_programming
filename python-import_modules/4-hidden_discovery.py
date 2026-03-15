#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # hidden_4 modulundakı bütün adları götürürük
    names = dir(hidden_4)
    
    # Əlifba sırası ilə sıralayırıq
    names.sort()
    
    for name in names:
        # Yalnız "__" ilə başlamayan adları çap edirik
        if not name.startswith("__"):
            print("{}".format(name))
