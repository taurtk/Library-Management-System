from flask import Blueprint, request, jsonify
from app.services.member_service import MemberService

member_bp = Blueprint('members', __name__)
member_service = MemberService()

@member_bp.route('/members', methods=['POST'])
def create_member():
    data = request.json
    member = member_service.create_member(data['name'])
    return jsonify({'member_id': member.member_id}), 201

@member_bp.route('/members', methods=['GET'])
def list_members():
    members = member_service.get_members()
    return jsonify([{'id': member.member_id, 'name': member.name} for member in members])

@member_bp.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = member_service.get_member(member_id)
    if member:
        return jsonify({'id': member.member_id, 'name': member.name})
    return jsonify({'error': 'Member not found'}), 404

@member_bp.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.json
    member = member_service.update_member(member_id, data['name'])
    if member:
        return jsonify({'id': member.member_id, 'name': member.name})
    return jsonify({'error': 'Member not found'}), 404

@member_bp.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = member_service.delete_member(member_id)
    if member:
        return jsonify({'message': 'Member deleted'}), 204
    return jsonify({'error': 'Member not found'}), 404