from flask import Flask
from config import Config
from database import db, ma
from routes import api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    ma.init_app(app)

    # Registra as rotas
    app.register_blueprint(api)

    # Cria o banco de dados se não existir
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    