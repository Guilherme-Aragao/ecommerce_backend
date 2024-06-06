
# controllers.py
"""
Curso de Engenharia de Software - UniEVANGÉLICA
Disciplina de Programação Web
Dev: Guilherme Aragão Silva
DATA: 06/06/2024
"""

from flask import request, jsonify
from app import app
from services import UserService, ProductService, OrderService

# Rota para registrar um novo usuário
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()  # Obtém os dados da requisição
    UserService.create_user(data['username'], data['password'])  # Cria um novo usuário
    return jsonify({'message': 'Usuário criado com sucesso'}), 201  # Retorna uma mensagem de sucesso

# Rota para login de usuário
@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()  # Obtém os dados da requisição
    if UserService.authenticate_user(data['username'], data['password']):  # Autentica o usuário
        return jsonify({'message': 'Login bem-sucedido'}), 200  # Retorna uma mensagem de sucesso
    return jsonify({'message': 'Credenciais inválidas'}), 401  # Retorna uma mensagem de erro

# Rota para adicionar um novo produto
@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()  # Obtém os dados da requisição
    ProductService.add_product(data['name'], data['price'])  # Adiciona um novo produto
    return jsonify({'message': 'Produto adicionado com sucesso'}), 201  # Retorna uma mensagem de sucesso

# Rota para criar uma nova ordem
@app.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()  # Obtém os dados da requisição
    OrderService.create_order(data['user_id'], data['product_id'], data['quantity'])  # Cria uma nova ordem
    return jsonify({'message': 'Ordem criada com sucesso'}), 201  # Retorna uma mensagem de sucesso

# Rota para obter todas as ordens de um usuário
@app.route('/orders/<int:user_id>', methods=['GET'])
def get_orders(user_id):
    orders = OrderService.get_user_orders(user_id)  # Obtém as ordens do usuário
    # Retorna as ordens em formato JSON
    return jsonify([{'id': order.id, 'product_id': order.product_id, 'quantity': order.quantity, 'total_price': order.total_price} for order in orders]), 200
