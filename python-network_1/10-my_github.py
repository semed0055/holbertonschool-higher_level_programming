#!/usr/bin/python3
"""Script that uses GitHub API with Basic Authentication to display
the user id corresponding to the given credentials"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(
        'https://api.github.com/user',
        auth=(sys.argv[1], sys.argv[2])
    )
    print(response.json().get('id'))
