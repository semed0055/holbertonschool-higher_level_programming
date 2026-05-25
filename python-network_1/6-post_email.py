#!/usr/bin/python3
"""Script that sends a POST request with an email parameter to a URL
and displays the body of the response using the requests package"""
import requests
import sys


if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
