# APi - É um lugar para disponibilizar recursos e ou funcionalidades
# Objetivo - Criar uma api de Criar, Alterar, Ler, Deletar um usuario de um determinado sistema 
# URL Base - localhost/user/v1/
# endpoints- 
        # -localhost/user/v1/ (GET)
        # -localhost/user/v1/id (GET)
        # -localhost/user/v1/id (PUT)
        # -localhost/user/v1/id (POST)
        # -localhost/user/v1/id (DELETE)
# Quais recursos - Cadastro e manipulação de dados cadastrais
from flask import Flask, jsonify, request

app = Flask(__name__)


users = [
    {
        'id': 1,
        'user_name':'Everton G',
        'name': 'Everton Garcia',
        'email': 'everton@garcia.com.br',
        'birth_date': '01/07/1995',
        'password': 'password'
    },
    {
        'id': 2,
        'user_name':'Paloma',
        'name': 'Paloma Garcia',
        'email': 'paloma@garcia.com.br',
        'birth_date': '28/11/1995',
        'password': 'minha senha'
    }
]

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    for user in users:
        if user.get('id') == id:
            return jsonify(user)

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    update_user = request.get_json()
    for i, user in enumerate(users):
        if user.get('id') == id:
            users[i].update(update_user)
            return jsonify(users[i])

@app.route('/users', methods=['POST'])
def create_user():
    create_user = request.get_json()
    users.append(create_user)
    
    return jsonify(users)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    for i, user in enumerate(users):
        if user.get('id') == id:
            del users[i]

    return jsonify(users)

app.run(port= 5000, host='localhost', debug=True)