from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Cria uma aplicação flask com o nome do arquivo atual
app = Flask(__name__)

# Instanciando o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Definindo/criando as tabelas no banco de dados
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(40), nullable=False)
    descricao = db.Column(db.String(130), nullable=False)

#Executa comandos da conexao com o BD


#Encerra conexão como banco de dados
#cursor.close()
#conexao.close()

#Comando sempre em aspas simples e se precisar passar um texto usar aspas duplas
##comando = '' #Escreve aqui o comando em sql
##cursor.Execute(comando) #executa o comando
##conexao.commit() # Necessário para comenado de edição no banco de dados
##ou
##resultado = cursor.fechtall() # Necessário para comandos de leituras no banco de dados



# Cria array de enquetes
enquetes = [
    {
        'id': 1,
        'titulo': 'Qual evento você gostaria que acontecesse na cidade?',
        'descricao': 'Vote no evento que você gostaria de ver na cidade',
        'opcoes': [
            {'id': 1, 'descricao': 'Show de música ao vivo', 'votos': 0},
            {'id': 2, 'descricao': 'Feira de artesanato', 'votos': 0},
            {'id': 3, 'descricao': 'Campeonato de esportes', 'votos': 0}
        ]
    },
    {
        'id': 2,
        'titulo': 'Qual sua opinião sobre o novo projeto de parque?',
        'descricao': 'Vote sobre o projeto do novo parque na cidade',
        'opcoes': [
            {'id': 1, 'descricao': 'Apoio ao projeto', 'votos': 0},
            {'id': 2, 'descricao': 'Contra o projeto', 'votos': 0}
        ]
    }
]

# 1. Criar enquete - POST
@app.route('/api/enquetes',methods=['POST'])
def criar_enquetes():
    data = request.get_json() # Pega os dados enviados na requisição no formato JSON e os converte em um dicionário
    nova_enquete = enquete(titulo=data['titulo'], descricao=data['email'])
    db.session.add(nova_enquete)
    

    return jsonify(enquetes)

# 2. Listar Enquetes - GET
@app.route('/api/enquetes',methods=['GET'])
def obter_enquetes():
    return jsonify(enquetes)

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
    for indice, enquete in enumerate(enquetes): 
        if enquete['id'] == id: #Acessa os IDs na lista e valida se é igual ao id passado
            del enquetes[indice]
            break  # Após deletar, interrompe o loop (não precisa continuar procurando)

    return jsonify(enquetes)

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
