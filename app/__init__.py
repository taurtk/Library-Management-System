from flask import Flask
from app.routes.book_routes import book_bp
from app.routes.member_routes import member_bp
# from app.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp)
    app.register_blueprint(member_bp)
    # app.register_blueprint(auth_bp)
    return app