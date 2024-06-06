
# app.py
"""
Curso de Engenharia de Software - UniEVANGÉLICA
Disciplina de Programação Web
Dev: Guilherme Aragão Silva
DATA: 06/06/2024
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Configura o banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

# Desativa o recurso de rastreamento de modificações para economizar recursos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Cria uma instância do SQLAlchemy para manipulação do banco de dados
db = SQLAlchemy(app)

# Executa a aplicação no modo de depuração
if __name__ == '__main__':
    app.run(debug=True)
