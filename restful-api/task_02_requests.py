#!/usr/bin/python3
"""Module for fetching and processing posts from JSONPlaceholder API"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches all posts from JSONPlaceholder and saves them to a CSV file"""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        data = [{'id': p.get('id'), 'title': p.get('title'),
                 'body': p.get('body')} for p in posts]
        with open('posts.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)
