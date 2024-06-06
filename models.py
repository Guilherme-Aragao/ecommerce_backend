
# models.py
"""
Curso de Engenharia de Software - UniEVANGÉLICA
Disciplina de Programação Web
Dev: Guilherme Aragão Silva
DATA: 06/06/2024
"""

from app import db

# Modelo de Usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Identificador único do usuário
    username = db.Column(db.String(80), unique=True, nullable=False)  # Nome de usuário único e obrigatório
    password = db.Column(db.String(120), nullable=False)  # Senha do usuário

# Modelo de Produto
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Identificador único do produto
    name = db.Column(db.String(80), nullable=False)  # Nome do produto, obrigatório
    price = db.Column(db.Float, nullable=False)  # Preço do produto, obrigatório

# Modelo de Ordem
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Identificador único da ordem
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Identificador do usuário que fez a ordem
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)  # Identificador do produto da ordem
    quantity = db.Column(db.Integer, nullable=False)  # Quantidade do produto na ordem
    total_price = db.Column(db.Float, nullable=False)  # Preço total da ordem
    user = db.relationship('User', backref=db.backref('orders', lazy=True))  # Relacionamento com o modelo User
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))  # Relacionamento com o modelo Product
