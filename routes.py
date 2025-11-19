from flask import Blueprint, request, jsonify, render_template
from database import db
from models import Book
from schemas import book_schema, books_schema

# Blueprint organiza as rotas
api = Blueprint('api', __name__)

# Rota para servir o Frontend
@api.route('/')
def index():
    return render_template('index.html')

# --- API ENDPOINTS ---

# Criar Livro
@api.route('/api/books', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    genre = request.json['genre']

    new_book = Book(title=title, author=author, genre=genre)
    db.session.add(new_book)
    db.session.commit()

    return book_schema.jsonify(new_book), 201

# Listar Livros (Com busca e filtro)
@api.route('/api/books', methods=['GET'])
def get_books():
    query = request.args.get('q') # Captura parametro de busca ?q=...
    
    if query:
        # Filtra por título ou autor (Case insensitive)
        results = Book.query.filter(
            (Book.title.ilike(f'%{query}%')) | 
            (Book.author.ilike(f'%{query}%'))
        ).all()
    else:
        results = Book.query.all()
        
    return books_schema.jsonify(results)

# Emprestar/Devolver Livro (Toggle)
@api.route('/api/books/<id>/toggle-loan', methods=['PUT'])
def toggle_loan(id):
    book = Book.query.get_or_404(id)
    book.is_loaned = not book.is_loaned
    db.session.commit()
    return book_schema.jsonify(book)

# Deletar Livro
@api.route('/api/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Livro removido com sucesso"})
