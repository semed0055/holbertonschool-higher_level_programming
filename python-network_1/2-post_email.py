#!/usr/bin/python3
"""Script that sends a POST request with an email parameter to a URL
and displays the body of the response decoded in utf-8"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
