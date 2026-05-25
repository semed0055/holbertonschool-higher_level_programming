#!/usr/bin/python3
"""Simple API built with Flask"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """Returns a welcome message"""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """Returns a list of all usernames stored in the API"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Returns the status of the API"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Returns the full object for the given username"""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the users dictionary"""
    try:
        data = request.get_json(force=True, silent=True)
        if data is None:
            return jsonify({"error": "Invalid JSON"}), 400
        username = data.get('username')
        if not username:
            return jsonify({"error": "Username is required"}), 400
        if username in users:
            return jsonify({"error": "Username already exists"}), 409
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400


if __name__ == "__main__":
    app.run()
