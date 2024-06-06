
# db_setup.py
"""
Curso de Engenharia de Software - UniEVANGÉLICA
Disciplina de Programação Web
Dev: Guilherme Aragão Silva
DATA: 06/06/2024
"""

from app import db
from models import User, Product, Order

# Cria todas as tabelas definidas nos modelos
db.create_all()
