from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Cria uma aplicação flask com o nome do arquivo atual
app = Flask(__name__)

# Instanciando o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Definindo/criando as tabelas no banco de dados
class Enquete(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(40), nullable=False)
    descricao = db.Column(db.String(130), nullable=False)

    # Sinaliza que a tabela "Enquete" terá um relacionamento com a tabela "Opcao"
    opcoes = db.relationship('Opcao', backref='enquete', lazy=True) # opcoes = db.relationship({nome da tabela que estará relacionada}, backref={tabela atual que irá se relacionar com outra tabela}, lazy=True)

    # Sinaliza que a tabela "Enquete" terá um relacionamento com a tabela "Voto"
    votos = db.relationship('Voto', backref='enquete', lazy=True)  # # votos = db.relationship({nome da tabela que estará relacionada}, backref={tabela atual que irá se relacionar com outra tabela}, lazy=True)

class Opcao(db.Model):
    opcao_id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(150), nullable=False)

    # Relacionamento com a tabela "Enquete"
    enquete_id = db.Column(db.Integer, db.ForeignKey('enquete.id'), nullable=False) # Cria a coluna enquete_id para armazenar o id da tabela "Enquete", o id da outra tabela é passado no parametro "enquete.id"
    # Sinaliza que a tabela "Opcao" terá um relacionamento com a tabela "Voto"
    votos = db.relationship('Voto', backref='opcao', lazy=True)  # # votos = db.relationship({nome da tabela que estará relacionada}, backref={tabela atual que irá se relacionar com outra tabela}, lazy=True)

class Voto(db.Model):
    voto_id = db.Column(db.Integer, primary_key = True)

    #Relacionamento com a tabela "Enquete"
    enquete_id = db.Column(db.Integer, db.ForeignKey('enquete.id'), nullable=False)
    #Relacionamento com a tabela "Opcao"
    opcao_id = db.Column(db.Integer, db.ForeignKey('opcao.opcao_id'), nullable=False)

    # Sinaliza que a tabela "Voto" terá um relacionamento com a tabela "Enquete"
    enquetes = db.relationship('Enquete', backref='Voto', lazy=True)
    # Sinaliza que a tabela "Voto" terá um relacionamento com a tabela "Opcao"
    opcoes = db.relationship('Opcao', backref='Voto', lazy=True)


#Comandos no banco
    #data = request.get_json()
    #nova_enquete = Enquete(titulo=data['titulo'], descricao=data['descricao'])
    #db.session.add = (comando) # Realiza o registro no banco de dados
    #db.session.commit() # Necessário para comenado de edição no banco de dados

# 1. Criar enquete - POST
@app.route('/api/enquetes',methods=['POST'])
def criar_enquetes():
    data = request.get_json() # Pega os dados enviados na requisição no formato JSON e os converte em um dicionário

    # Verifica se os campos 'titulo' e 'descricao' estão presentes no JSON
    if 'titulo' not in data or 'descricao' not in data:
        return jsonify({"erro": "Campos 'titulo' e 'descricao' são obrigatórios."}), 400

    nova_enquete = Enquete(titulo=data['titulo'], descricao=data['descricao'])
    db.session.add(nova_enquete)
    db.session.commit()
    
    return jsonify({"mensagem": "Enquete criada com sucesso."}), 201

# 2. Listar Enquetes - GET
@app.route('/api/enquetes',methods=['GET'])
def obter_enquetes():
    enquetes = Enquete.query.all()
    enquete_lista = []
    for enquete in enquetes:
        enquete_data = {
            "id": enquete.id,
            "titulo": enquete.titulo,
            "descricao": enquete.descricao
        }
        enquete_lista.append(enquete_data)
    return jsonify(enquete_lista), 200

# 3. Obter detalhes de uma enquete - GET
@app.route('/api/enquetes/<int:id>',methods=['GET'])
def obter_enquetes_por_id(id): #esse método recebe por parametro o id da enquete
    enquetes = Enquete.query.get(id)
    
    if enquetes: # Se a enquete for encontrada
        enquete_data = {
            "id": enquetes.id,
            "titulo": enquetes.titulo,
            "descricao": enquetes.descricao
        }
        return jsonify(enquete_data), 200  # Retorna os dados da enquete encontrada
    
    return jsonify({"erro": "Enquete não encontrada."}), 404  # Retorna erro se a enquete não for encontrada

# 4. Votar em uma opção de enquete - POST
@app.route('/api/enquetes/<int:id>/votar',methods=['POST'])
def votar_enquete(opcao_id):

    #obtem os dados da requsição
    data = request.get_json()

    #Valida se a opção de voto foi fornecida
    if 'opcao_id' not in data:
        return jsonify({"error": "É necessário selecionar uma opção"}), 400

    opcao_id = data['opcao_id']

    # Verifica se a opção existe
    opcao = Opcao.query.get(opcao_id)
    if not opcao:
        return jsonify({"error": "Opção de voto não encontrada"}), 404

    # Cria o novo voto
    novo_voto = Voto(enquete_id=id, opcao_id=opcao_id)
    db.session.add(novo_voto)  # Adiciona o voto na sessão e comita
    db.session.commit()
    
    # Retorna uma resposta de sucesso
    return jsonify({"mensagem": "Voto registrado com sucesso!"}), 201

# 5. Resultados de uma enquete
#@app.route('/api/enquetes/<int:id>/resultados',methods=['GET'])

# 6. Visualizar opções de uma enquete
#@app.route('/api/enquetes/<int:id>/opcoes',methods=['GET'])

# 7. Adicionar a opção em uma enquete
@app.route('/api/enquetes/<int:id>/opcoes',methods=['POST'])
def criar_opcoes(id):
    data = request.get_json() # Pega os dados enviados na requisição no formato JSON e os converte em um dicionário

    # Verifica se os campos 'titulo' e 'descricao' estão presentes no JSON
    if 'titulo' not in data:
        return jsonify({"erro": "A descrição é obrigatória."}), 400

    nova_opcao = Opcao(titulo=data['titulo'], enquete_id=id)
    db.session.add(nova_opcao)
    db.session.commit()
    
    return jsonify({"mensagem": "Opção criada com sucesso."}), 201

# 8. Deletar enquete
@app.route('/api/enquetes/<int:id>', methods=['DELETE'])
def deletar_enquete_por_id(id): #esse método recebe por parametro o id da enquete
    enquete = Enquete.query.get(id) #{nome metodo} = {nome tabela}.query.get.({id recebido no parametro})

    #Valida se id existe e realiza a exclusão
    if enquete:
        db.session.delete(enquete)
        db.session.commit()
        return jsonify({"mensagem": "Enquete excluída com sucesso."}), 200
    else:
        return jsonify({"Mensagem": "Enquete não encontrada"}), 404

# 9. Deletar uma opção de uma enquete
#@app.route('/api/enquetes/<int:id>/opcoes/{id_opcao}',methods=['DELETE'])

#@app.route('/api/enquetes/<int:id>/opcoes',methods=['GET'])
#def opcoes_enquete(id): #esse método recebe por parametro o id da enquete
#    nova_opcao = request.get_json()
#    for indice,livro in enumerate(enquetes):
#        if enquente.get('id') == id:
#            enquetes.update(nova_opcao)
#            return jsonify(livros[indice])

if __name__ == '__main__':
    # Cria as tabelas do modelo
    with app.app_context():
        db.create_all()

    #Sube aplicação na porta 5000
    app.run(port=5000,host='localhost',debug=True)
