from app.models.book import Book

class BookService:
    def __init__(self):
        self.books = {}
        self.counter = 1

    def create_book(self, title, author):
        book = Book(self.counter, title, author)
        self.books[self.counter] = book
        self.counter += 1
        return book

    def get_books(self, page=1, per_page=10):
        start = (page - 1) * per_page
        end = start + per_page
        return list(self.books.values())[start:end]

    def get_book(self, book_id):
        return self.books.get(book_id)

    def update_book(self, book_id, title, author):
        if book_id in self.books:
            self.books[book_id].title = title
            self.books[book_id].author = author
            return self.books[book_id]
        return None

    def delete_book(self, book_id):
        return self.books.pop(book_id, None)

    def search_books(self, query):
        return [book for book in self.books.values() if query.lower() in book.title.lower() or query.lower() in book.author.lower()]