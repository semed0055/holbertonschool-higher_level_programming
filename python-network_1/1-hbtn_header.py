#!/usr/bin/python3
"""Sends a request to a URL and displays the X-Request-Id header value"""
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url, headers={'cfclearance': 'true'})
with urllib.request.urlopen(req) as response:
    print(response.headers.get('X-Request-Id'))
