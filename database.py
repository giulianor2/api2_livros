from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

'''
    A biblioteca Marshmallow é um tradutor. Ela pega o objeto do banco e converte ("serializa") para JSON, e pega o JSON que o 
    usuário enviou e converte ("desserializa") para objeto Python, validando os dados no processo.
'''
