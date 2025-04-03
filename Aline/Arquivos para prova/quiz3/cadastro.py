from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

ARQUIVO_USUARIOS = 'usuarios.json'
contador_id = 1

# Função para carregar usuários do arquivo
def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# Função para salvar usuários no arquivo
def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4)

# Inicializa o contador_id com base nos usuários existentes
def inicializar_contador():
    global contador_id
    usuarios = carregar_usuarios()
    if usuarios:
        contador_id = max(usuario['id'] for usuario in usuarios) + 1

# Rota para cadastrar novo usuário
@app.route("/usuarios", methods=["POST"])
def cadastrar_usuario():
    global contador_id
    dados = request.get_json()

    if not dados or "usuario" not in dados:
        return jsonify({"erro": "O campo 'usuario' é obrigatório."}), 400

    usuarios = carregar_usuarios()
    
    novo_usuario = {
        "id": contador_id,
        "usuario": dados["usuario"]
    }

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    
    contador_id += 1
    return jsonify(novo_usuario), 201

# Rota para listar todos os usuários
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = carregar_usuarios()
    return jsonify(usuarios)

# Rota para obter um usuário específico
@app.route("/usuarios/<int:id>", methods=["GET"])
def obter_usuario(id):
    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u['id'] == id), None)
    
    if usuario:
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# Rota para atualizar um usuário
@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    dados = request.get_json()
    
    if not dados or "usuario" not in dados:
        return jsonify({"erro": "O campo 'usuario' é obrigatório."}), 400

    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u['id'] == id), None)
    
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    
    usuario['usuario'] = dados['usuario']
    salvar_usuarios(usuarios)
    
    return jsonify(usuario)

# Rota para deletar um usuário
@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    usuarios = carregar_usuarios()
    usuario = next((u for u in usuarios if u['id'] == id), None)
    
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    
    usuarios = [u for u in usuarios if u['id'] != id]
    salvar_usuarios(usuarios)
    
    return jsonify({"mensagem": "Usuário deletado com sucesso"}), 200

# Inicializa o contador de IDs quando o servidor começa
inicializar_contador()

if __name__ == '__main__':
    app.run(debug=True, port=5002)