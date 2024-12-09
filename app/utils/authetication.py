from flask import request, jsonify

class AuthService:
    def __init__(self):
        self.tokens = {}

    def generate_token(self, username):
        token = f"token-{username}"
        self.tokens[token] = username
        return token

    def validate_token(self, token):
        return token in self.tokens