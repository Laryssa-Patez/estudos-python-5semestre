from flask import Flask, jsonify, request

# Cria uma aplicação flask com o nome do arquivo atual
app = Flask(__name__)

# Cria array de enquetes

enquetes = [
    {
        'id': 1,
        'Título':'Enquete Exemplo',
        'Descrição':'Descrição Exemplo',
        'Status':'Ativa',
        'Categoria':'Cultura'
    },
    {
        'id': 2,
        'Título':'Enquete Exemplo 2',
        'Descrição':'Descrição Exemplo',
        'Status':'Ativa',
        'Categoria':'Cultura'
    }
]

# Criar enquete - POST

#Listar enquetes - GET
@app.route('/api/enquetes',methods=['GET'])
def obter_enquetes():
    return jsonify(enquetes)

#Apagar enquetes por ID - 


#Subir aplicação na porta 5000
app.run(port=5000,host='localhost',debug=True)