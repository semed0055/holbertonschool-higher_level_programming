#!/usr/bin/python3
"""Script that sends a request to a URL and displays the response body,
printing the HTTP error code if status code is 400 or greater"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
