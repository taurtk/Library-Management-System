from flask import Blueprint, request, jsonify
from app.services.book_service import BookService

book_bp = Blueprint('books', __name__)
book_service = BookService()

@book_bp.route('/books', methods=['POST'])
def create_book():
    data = request.json
    book = book_service.create_book(data['title'], data['author'])
    return jsonify({'book_id': book.book_id}), 201

@book_bp.route('/books', methods=['GET'])
def list_books():
    page = request.args.get('page', 1, type=int)
    books = book_service.get_books(page)
    return jsonify([{'id': book.book_id, 'title': book.title, 'author': book.author} for book in books])

@book_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = book_service.get_book(book_id)
    if book:
        return jsonify({'id': book.book_id, 'title': book.title, 'author': book.author})
    return jsonify({'error': 'Book not found'}), 404

@book_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = book_service.update_book(book_id, data['title'], data['author'])
    if book:
        return jsonify({'id': book.book_id, 'title': book.title, 'author': book.author})
    return jsonify({'error': 'Book not found'}), 404

@book_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = book_service.delete_book(book_id)
    if book:
        return jsonify({'message': 'Book deleted'}), 204
    return jsonify({'error': 'Book not found'}), 404

@book_bp.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '')
    books = book_service.search_books(query)
    return jsonify([{'id': book.book_id, 'title': book.title, 'author': book.author} for book in books])