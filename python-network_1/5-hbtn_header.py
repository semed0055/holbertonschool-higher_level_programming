#!/usr/bin/python3
"""Script that sends a request to a URL and displays the X-Request-Id
value from the response header using the requests package"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1], headers={'cfclearance': 'true'})
    print(response.headers.get('X-Request-Id'))
