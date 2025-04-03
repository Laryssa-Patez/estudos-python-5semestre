from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bauru_participa.db'
db = SQLAlchemy(app)

#Modelos do Banco de dados
class Enquete(db.Model): #criando uma classe herdada da classe Model, transformando a classe em uma tabela do banco de dados
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    data_criacao = db.Column(db.DateTime, server_default=db.func.now())
    opcoes = db.relationship('Opcao', backref='enquete', lazy=True)

class Opcao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(100), nullable=False)
    votos = db.Column(db.Integer, default=0)
    id_enquete = db.Column(db.Integer, db.ForeignKey('enquete.id'))

#with app.app_context():
#    db.drop_all()  # Apaga todas as tabelas
#    db.create_all()  # Recria tudo do zero

#Cria o banco de dados
with app.app_context():
    db.create_all() #cria as tabelas no banco


@app.route('/api/enquetes', methods=['POST'])
def criar_enquete():
    dados = request.get_json()
    nova_enquete = Enquete(
        titulo=dados['titulo'],
        descricao=dados.get('descricao', ''),
        
    )
    db.session.add(nova_enquete)
    db.session.commit()
    return jsonify({"mensagem": "Enquete criada com sucesso!", "id": nova_enquete.id}), 201

#precisa criar a header Content-Type: application/json
#em body (raw JSON) devemos adicionar:
#{
#    "titulo": "Deve ter mais ciclovias?",
#    "descricao": "Votação sobre expansão de ciclovias no centro"
#}


@app.route('/api/enquetes', methods=['GET']) 
def listar_enquetes():
    enquetes = Enquete.query.all()
    resultado = []
    for enquete in enquetes:
        resultado.append({
            "id": enquete.id,
            "titulo": enquete.titulo,
            "descricao": enquete.descricao
        })
    return jsonify(resultado)

@app.route('/api/enquetes/<int:id>', methods=['GET']) #no <int:id> colocar o id da enquete que quer detalhar
def detalhes_enquete(id):
    enquete = Enquete.query.get_or_404(id)
    return jsonify({
        "id": enquete.id,
        "titulo": enquete.titulo,
        "descricao": enquete.descricao
    })

@app.route('/api/enquetes/<int:enquete_id>/votar', methods=['POST'])
def votar(enquete_id):
    dados = request.get_json()  # obtém os dados JSON enviados na requisição
    
    # verificação básica do JSON
    # checa se o JSON foi recebido e se contém o campo obrigatório 'opcao_id':
    if not dados or 'opcao_id' not in dados:
        return jsonify({"erro": "O campo 'opcao_id' é obrigatório"}), 400 # retorna erro 400 (Bad Request) se a validação falhar
    
    try:
        # busca a opção no banco de dados verificando:
        # 1. se existe uma opção com o ID recebido (dados['opcao_id'])
        # 2. se essa opção pertence à enquete especificada (id_enquete=enquete_id)
        opcao = Opcao.query.filter_by(
            id=dados['opcao_id'], # ID da opção recebido no JSON
            id_enquete=enquete_id  # deve pertencer à enquete da URL
        ).first() # pega o primeiro resultado ou None
        
        if not opcao:  # se não encontrou a opção ou não pertence à enquete
            return jsonify({"erro": "Opção não encontrada nesta enquete"}), 404 # retorna erro 404 (Not Found)
        
        # incrementa o contador de votos de forma thread-safe
        # usa Opcao.votos + 1 ao invés de += 1 para evitar race conditions (condição de corrida -
        # para nao perder votos se ocorrer votação simultânea)
        opcao.votos = Opcao.votos + 1
        db.session.commit() # Confirma a transação no banco de dados
        
        # retorna resposta de sucesso com informações relevantes
        return jsonify({
            "mensagem": "Voto registrado!",
            "opcao": opcao.texto,
            "novo_total": opcao.votos
        })
        
    except Exception as e: # em caso de qualquer erro inesperado:
        db.session.rollback() # desfaz operações não confirmadas
        return jsonify({"erro": str(e)}), 500 # retorna erro 500 (Internal Server Error)

#{
#    "opcao_id": 1
#}

@app.route('/api/enquetes/<int:id>/resultados', methods=['GET'])
def resultados(id):
    opcoes = Opcao.query.filter_by(id_enquete=id).all()
    resultado = []
    for opcao in opcoes:
        resultado.append({
            "opcao": opcao.texto,
            "votos": opcao.votos
        })
    return jsonify(resultado)

@app.route('/api/enquetes/<int:id>/opcoes', methods=['GET'])
def opcoes_enquete(id):
    opcoes = Opcao.query.filter_by(id_enquete=id).all()
    return jsonify([{"id": op.id, "texto": op.texto} for op in opcoes])

@app.route('/api/enquetes/<int:id>/opcoes', methods=['POST'])
def adicionar_opcao(id):
    dados = request.get_json()
    nova_opcao = Opcao(
        texto=dados['texto'],
        id_enquete=id
    )
    db.session.add(nova_opcao)
    db.session.commit()
    return jsonify({"mensagem": "Opção adicionada!"}), 201

#{
#    "texto": "Sim"
#}

@app.route('/api/enquetes/<int:id>', methods=['DELETE'])
def deletar_enquete(id):
    enquete = Enquete.query.get_or_404(id)
    db.session.delete(enquete)
    db.session.commit()
    return jsonify({"mensagem": "Enquete deletada!"})

@app.route('/api/enquetes/<int:id_enquete>/opcoes/<int:id_opcao>', methods=['DELETE'])
def deletar_opcao(id_enquete, id_opcao):
    opcao = Opcao.query.get_or_404(id_opcao)
    db.session.delete(opcao)
    db.session.commit()
    return jsonify({"mensagem": "Opção deletada!"})

if __name__ == '__main__':
    app.run(port=5001, debug=True)