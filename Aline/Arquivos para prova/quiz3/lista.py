from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = []

contador_id = 1

@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    global contador_id

    dados = request.get_json()

    if not dados or "descricao" not in dados:
        return jsonify({"erro": "O campo 'descricao' é obrigatório."}), 400

    nova_tarefa = {
        "id": contador_id,
        "descricao": dados["descricao"],
        "concluida": False
    }

    tarefas.append(nova_tarefa)

    contador_id += 1

    return jsonify(nova_tarefa), 201

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas/<int:id>/concluir", methods=["PUT"])
def concluir_tarefa(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)

    if tarefa is None:
        return jsonify({"erro": "Tarefa não encontrada."}), 404

    tarefa["concluida"] = True

    return jsonify(tarefa)

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def excluir_tarefa(id):
    global tarefas

    tarefa = next((t for t in tarefas if t["id"] == id), None)

    if tarefa is None:
        return jsonify({"erro": "Tarefa não encontrada."}), 404

    tarefas = [t for t in tarefas if t["id"] != id]

    return jsonify({"mensagem": "Tarefa excluída com sucesso."}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5002)