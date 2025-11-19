from database import ma
from models import Book

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True

book_schema = BookSchema()
books_schema = BookSchema(many=True)
