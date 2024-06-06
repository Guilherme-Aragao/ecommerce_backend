
# repositories.py
"""
Curso de Engenharia de Software - UniEVANGÉLICA
Disciplina de Programação Web
Dev: Guilherme Aragão Silva
DATA: 06/06/2024
"""

from models import User, Product, Order
from app import db

# Repositório de Usuário
class UserRepository:
    @staticmethod
    def add_user(username, password):
        # Adiciona um novo usuário ao banco de dados
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def get_user_by_username(username):
        # Busca um usuário pelo nome de usuário
        return User.query.filter_by(username=username).first()

# Repositório de Produto
class ProductRepository:
    @staticmethod
    def add_product(name, price):
        # Adiciona um novo produto ao banco de dados
        new_product = Product(name=name, price=price)
        db.session.add(new_product)
        db.session.commit()

    @staticmethod
    def get_product_by_id(product_id):
        # Busca um produto pelo ID
        return Product.query.get(product_id)

# Repositório de Ordem
class OrderRepository:
    @staticmethod
    def add_order(user_id, product_id, quantity, total_price):
        # Adiciona uma nova ordem ao banco de dados
        new_order = Order(user_id=user_id, product_id=product_id, quantity=quantity, total_price=total_price)
        db.session.add(new_order)
        db.session.commit()

    @staticmethod
    def get_orders_by_user_id(user_id):
        # Busca todas as ordens de um usuário pelo ID do usuário
        return Order.query.filter_by(user_id=user_id).all()
