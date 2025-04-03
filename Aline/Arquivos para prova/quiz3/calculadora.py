from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculadora/adicao", methods=["GET"])
def adicao(): # def = funçao/método quando eu chamar a url /calculadora/adicao o método que será chamado será o a seguir:
    num1 = request.args.get("num1", type=float)
    num2 = request.args.get("num2", type=float)
    soma = num1 + num2
    dados = {"resultado": soma}
    return jsonify(dados),200

@app.route("/calculadora/subtracao", methods=["GET"])
def subtracao():
    num1 = request.args.get("num1", type=float)
    num2 = request.args.get("num2", type=float)
    subtracao = num1 - num2
    dados = {"resultado": subtracao}
    return jsonify(dados),200

@app.route("/calculadora/multiplicacao", methods=["GET"])
def multiplicacao():
    num1 = request.args.get("num1", type=float)
    num2 = request.args.get("num2", type=float)
    multiplicacao = num1 * num2
    dados = {"resultado": multiplicacao}
    return jsonify(dados),200

@app.route("/calculadora/divisao", methods=["GET"])
def divisao():
    num1 = request.args.get("num1", type=float)
    num2 = request.args.get("num2", type=float)
    if num2 == 0:
        return jsonify({"erro": "Não é permitida divisão por 0."}),422
    divisao = num1 / num2
    dados = {"resultado": divisao}
    return jsonify(dados),200


if __name__ == '__main__':
    app.run(debug = True, port=5002)
