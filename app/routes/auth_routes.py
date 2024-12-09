from flask import Blueprint, request, jsonify
from app.utils.authentication import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    token = auth_service.generate_token(data['username'])
    return jsonify({'token': token}), 200

@auth_bp.route('/auth/logout', methods=['POST'])
def logout():
    data = request.json
    # Invalidate token logic can be added here
    return jsonify({'message': 'Logged out'}), 200