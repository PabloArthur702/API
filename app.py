# API - é um lugar para disponibilizar recursos e/ou funcionalidades


from flask import Flask, jsonify , request

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

from datetime import datetime, timedelta
import uuid

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super_secret_key"  # Chave secreta para o JWT
jwt = JWTManager(app)

users = [] #{"name": "João","password": "1234"}

tasks = [] #{"id": 1,"name": "tasks 1","descrição": "Descrição 1","deadline":"2024-12-09 23:59:00","done": False}

#Funções de busca
#Busca de usuário
def find_user(name):
    for user in users:
        if user["name"] == name:
            return user
    return None

#Busca de task
def find_task(id, name):
    for task in tasks:
        if task["id"] == str(id) and task["name"] == name:
            return task
    return None

#Rotas de usuario
#Cadastro
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    name = data.get("name")
    password = data.get("password")
    
    if find_user(name):
        return jsonify(message="Usuário já existe"), 400
    users.append({
        "name": name,
        "password": password
    })
    return jsonify(message="Usuário cadastrado com sucesso"), 201

#Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    name = data.get('name')
    password = data.get('password')
    
    user = find_user(name)
    if user and user["password"] == password:
        access_token = create_access_token(identity=name, expires_delta=timedelta(minutes=120))
        return jsonify({"access_token": access_token}), 200
    return jsonify({"message": "Credenciais inválidas"}), 401

#Rotas de tasks

#Adicionar um nova task
@app.route('/tasks', methods=['POST'])
@jwt_required()
def add_task():
    current_user = get_jwt_identity()
    data = request.json

    new_task = {
        "id": str(uuid.uuid4()),
        "name": current_user,
        "title": data.get("title"),
        "description": data.get("description"),
        "deadline": datetime.strptime(data.get("deadline"), "%Y-%m-%d %H:%M:%S"),
        "done": False,
    }
    tasks.append(new_task)
    return jsonify({"message": "Tarefa adicionada com sucesso", "task": new_task}), 201

#Consultar(Todos)
@app.route('/tasks', methods=['GET'])
@jwt_required()
def obter_tasks():
    current_user = get_jwt_identity()
    user_tasks = [task for task in tasks if task["name"] == current_user]
    return jsonify(user_tasks), 200

#consultar(id)
@app.route('/tasks/<id>', methods=['GET'])
@jwt_required()
def obter_task_por_id(id):
    current_user = get_jwt_identity()
    task = find_task(id, current_user)
    if task:
        return jsonify(task), 200 
    return jsonify({"message": "Tarefa não encontrada"}), 404

#editar
@app.route('/tasks/<id>', methods=['PUT'])
@jwt_required()
def editar_task(id):
    current_user = get_jwt_identity()
    task = find_task(id, current_user)
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    
    data = request.json
    task["title"] = data.get("title", task["title"])
    task["description"] = data.get("description", task["description"])
    task["deadline"] = datetime.strptime(data.get("deadline"), "%Y-%m-%d %H:%M:%S")
    return jsonify({"message": "Tarefa atualizada com sucesso", "task": task}), 200

#marcar como feito
@app.route('/tasks/<id>/done', methods=['PUT'])
@jwt_required()
def mark_done(id):
    current_user = get_jwt_identity()
    task = find_task(id, current_user)
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    task["done"] = True
    return jsonify({"message": "Tarefa marcada como feita", "task": task}), 200

#excluir
@app.route('/tasks/<id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    current_user = get_jwt_identity()
    task = find_task(id, current_user)
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"}), 200

#Notificação
@app.route('/notifications', methods=['GET'])
@jwt_required()
def get_notifications():
    current_user = get_jwt_identity()
    notifications = [
        task
        for task in tasks
        if task["name"] == current_user and not task["done"] and 0 <= (task["deadline"] - datetime.now()).days <= 3
    ]
    return jsonify(notifications), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)