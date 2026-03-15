#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    # sys.argv[0] skriptin adıdır, ona görə [1:] ilə başlayırıq
    for arg in sys.argv[1:]:
        total += int(arg)
    print("{}".format(total))
