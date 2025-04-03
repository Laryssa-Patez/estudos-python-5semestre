from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

contador_id = 1

@app.route("/cadastro", methods=["POST"])
def cadastro():
    global contador_id

    dados = request.get_json()

    if not dados or "usuario" not in dados:
        return jsonify({"erro": "O campo 'usuario' é obrigatório."}),400

    novo_usuario = {
        "id": contador_id,
        "usuario": dados["usuario"]
    }

    usuarios.append(novo_usuario)

    contador_id += 1

    return jsonify(novo_usuario),201

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True, port=5002)