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

#Comandos no banco
    #data = request.get_json()
    #nova_enquete = Enquete(titulo=data['titulo'], descricao=data['descricao'])
    #db.session.add = (comando) # Realiza o registro no banco de dados
    #db.session.commit() # Necessário para comenado de edição no banco de dados


# Cria array de enquetes
#enquetes = [
    #{
        #'id': 1,
        #'titulo': 'Qual evento você gostaria que acontecesse na cidade?',
        #'descricao': 'Vote no evento que você gostaria de ver na cidade',
        #'opcoes': [
            #{'id': 1, 'descricao': 'Show de música ao vivo', 'votos': 0},
            #{'id': 2, 'descricao': 'Feira de artesanato', 'votos': 0},
            #{'id': 3, 'descricao': 'Campeonato de esportes', 'votos': 0}
        #]
    #},
#]

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
    for enquente in enquetes: 
        if enquente['id'] == id: #Acessa os IDs na lista e valida se é igual ao id passado
            return jsonify(enquente)

# 4. Votar em uma opção de enquete - POST
#@app.route('/api/enquetes/<int:id>/votar',methods=['POST'])

# 5. Resultados de uma enquete
#@app.route('/api/enquetes/<int:id>/resultados',methods=['GET'])

# 6. Visualizar opções de uma enquete
#@app.route('/api/enquetes/<int:id>/opcoes',methods=['GET'])

# 7. Adicionar a opção em uma enquete
#@app.route('/api/enquetes/<int:id>/opcoes',methods=['POST'])

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
