#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using urllib"""
import urllib.request

url = 'https://intranet.hbtn.io/status'
req = urllib.request.Request(url, headers={'cfclearance': 'true'})
with urllib.request.urlopen(req) as response:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
