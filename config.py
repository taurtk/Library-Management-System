
class Config:
    """Application configuration settings"""
    SECRET_KEY = 'your_secret_key_here'  # Replace with a secure random key in production
    TOKEN_EXPIRATION_MINUTES = 60
    MAX_ITEMS_PER_PAGE = 10