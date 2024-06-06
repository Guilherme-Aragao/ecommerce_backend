
# services.py
"""
Curso de Engenharia de Software - UniEVANGÉLICA
Disciplina de Programação Web
Dev: Guilherme Aragão Silva
DATA: 06/06/2024
"""

from repositories import UserRepository, ProductRepository, OrderRepository

# Serviço de Usuário
class UserService:
    @staticmethod
    def create_user(username, password):
        # Cria um novo usuário utilizando o UserRepository
        UserRepository.add_user(username, password)

    @staticmethod
    def authenticate_user(username, password):
        # Autentica um usuário verificando o nome de usuário e senha
        user = UserRepository.get_user_by_username(username)
        if user and user.password == password:
            return True
        return False

# Serviço de Produto
class ProductService:
    @staticmethod
    def add_product(name, price):
        # Adiciona um novo produto utilizando o ProductRepository
        ProductRepository.add_product(name, price)

    @staticmethod
    def get_product(product_id):
        # Busca um produto pelo ID utilizando o ProductRepository
        return ProductRepository.get_product_by_id(product_id)

# Serviço de Ordem
class OrderService:
    @staticmethod
    def create_order(user_id, product_id, quantity):
        # Cria uma nova ordem calculando o preço total
        product = ProductRepository.get_product_by_id(product_id)
        total_price = product.price * quantity
        OrderRepository.add_order(user_id, product_id, quantity, total_price)

    @staticmethod
    def get_user_orders(user_id):
        # Busca todas as ordens de um usuário
        return OrderRepository.get_orders_by_user_id(user_id)
