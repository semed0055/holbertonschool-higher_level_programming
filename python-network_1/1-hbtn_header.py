#!/usr/bin/python3
"""Script that takes a URL, sends a request, and displays the X-Request-Id
header value from the response"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url, headers={'cfclearance': 'true'})
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
