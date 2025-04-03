from flask import Flask, request, jsonify

app = Flask(__name__)

produtos = []

carrinho = []

contador_id = 1

@app.route("/produtos", methods=["POST"])
def adicionar_produto():
    global contador_id

    dados = request.get_json()

    if not dados or "nome" not in dados or "preco" not in dados or "estoque" not in dados:
        return jsonify({"erro": "Os campos 'nome', 'preco' e 'estoque' são obrigatórios."}), 400

    novo_produto = {
        "id": contador_id,
        "nome": dados["nome"],
        "preco": dados["preco"],
        "estoque": dados["estoque"]
    }

    produtos.append(novo_produto)

    contador_id += 1

    return jsonify(novo_produto), 201

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

@app.route("/produtos/<int:id>/estoque", methods=["PUT"])
def atualizar_estoque(id):
    produto = next((p for p in produtos if p["id"] == id), None)

    if produto is None:
        return jsonify({"erro": "Produto não encontrado."}), 404

    dados = request.get_json()
    
    if "estoque" not in dados:
        return jsonify({"erro": "O campo 'estoque' é obrigatório."}), 400
    
    produto["estoque"] = dados["estoque"]

    return jsonify(produto)


@app.route("/produtos/<int:id>", methods=["DELETE"])
def excluir_produto(id):
    global produtos
    
    produto = next((p for p in produtos if p["id"] == id), None)
    
    if produto is None:
        return jsonify({"erro": "Produto não encontrado."}), 404
    
    produtos = [p for p in produtos if p["id"] != id]
    
    return jsonify({"mensagem": "Produto excluído com sucesso."}), 200

@app.route("/carrinho", methods=["POST"])
def adicionar_ao_carrinho():
    dados = request.get_json()

    if not dados or "produto_id" not in dados or "quantidade" not in dados:
        return jsonify({"erro": "Os campos 'produto_id' e 'quantidade' são obrigatórios."}), 400

    produto = next((p for p in produtos if p["id"] == dados["produto_id"]), None)

    if produto is None:
        return jsonify({"erro": "Produto não encontrado."}), 404

    if produto["estoque"] < dados["quantidade"]:
        return jsonify({"erro": "Estoque insuficiente."}), 400

    carrinho.append({
        "produto_id": produto["id"],
        "nome": produto["nome"],
        "preco": produto["preco"],
        "quantidade": dados["quantidade"]
    })

    return jsonify(carrinho), 201

@app.route("/carrinho", methods=["GET"])
def listar_carrinho():
    return jsonify(carrinho)

@app.route("/carrinho/<int:id>", methods=["DELETE"])
def remover_do_carrinho(id):
    global carrinho

    item = next((i for i in carrinho if i["produto_id"] == id), None)

    if item is None:
        return jsonify({"erro": "Item não encontrado no carrinho."}), 404

    carrinho = [i for i in carrinho if i["produto_id"] != id]

    return jsonify({"mensagem": "Item removido do carrinho com sucesso."}), 200

@app.route("/carrinho/finalizar", methods=["POST"])
def finalizar_compra():
    global carrinho, produtos

    if not carrinho:
        return jsonify({"erro": "O carrinho está vazio."}), 400

    for item in carrinho:
        produto = next((p for p in produtos if p["id"] == item["produto_id"]), None)
        if produto:
            produto["estoque"] -= item["quantidade"]

    carrinho.clear()

    return jsonify({"mensagem": "Compra finalizada com sucesso."}), 200

if __name__ == '__main__':
    app.run(debug=True)