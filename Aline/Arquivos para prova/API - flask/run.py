from flask import Flask, request, jsonify
# flask é um mini framework que ajuda na criaçao de apis
# request representa a requisiçao (quando vc chama (acessa a url) a sua api) do navegador ou postman 
# jsonify é para formatar os dados em json

app = Flask(__name__)

@app.route('/aline')
def index():
    return 'Bem-vindo à sua API simples com Flask!'

#127.0.0.1 ou localhost apontam para a minha maquina

# url.com.br/api/parametro?nome=aline&time=Palmeiras

@app.route('/api/parametro', methods=['GET'])
def exemplo_parametro():
    nome = request.args.get('nome', 'Visitante')
    dados = {'mensagem': f'Ólá, {nome}!'}
    return jsonify(dados), 200

@app.route('/api/payload', methods=['POST'])
def receber_payload():
    try:
        payload = request.get_json()
        return jsonify({"mensagem": "Payload recebido com sucesso", "payload": payload}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(debug = True, port=5002)

