from flask import Flask, jsonify, request

# Cria uma aplicação flask com o nome do arquivo atual
app = Flask(__name__)

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
# 5. Resultados de uma enquete
# 6. Visualizar opções de uma enquete
# 7. Adicionar a opção em uma enquete
# 8. Deletar enquete
# 9. Deletar uma opção de uma enquete


#@app.route('/api/enquetes/<int:id>/opcoes',methods=['GET'])
#def opcoes_enquete(id): #esse método recebe por parametro o id da enquete
#    nova_opcao = request.get_json()
#    for indice,livro in enumerate(enquetes):
#        if enquente.get('id') == id:
#            enquetes.update(nova_opcao)
#            return jsonify(livros[indice])

#Subir aplicação na porta 5000
app.run(port=5000,host='localhost',debug=True)