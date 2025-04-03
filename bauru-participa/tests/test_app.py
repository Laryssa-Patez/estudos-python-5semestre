import pytest
from app import app, db, Enquete  # Importa sua aplicação Flask e os modelos

# Entrada -> Elemento (teste) -> Prever uma saída

@pytest.fixture
def client():
    app.config['TESTING'] = True # Isso impede que exceções interrompam a execução dos testes.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Banco em memória
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Cria tabelas para o teste
        yield client  # Retorna o cliente de teste

def test_criar_enquete(client):
    """Teste para criar uma enquete"""
    response = client.post('/api/enquetes', json={
        "titulo": "Melhor linguagem?",
        "descricao": "Escolha sua linguagem favorita"
    })
    assert response.status_code == 201
    assert response.get_json() == {"mensagem": "Enquete criada com sucesso."}

def test_obter_enquetes(client):
    """Teste para listar enquetes"""
    # Criando uma enquete diretamente no banco
    with app.app_context():
        nova_enquete = Enquete(titulo="Melhor framework?", descricao="Escolha um framework")
        db.session.add(nova_enquete)
        db.session.commit()

    response = client.get('/api/enquetes')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['titulo'] == "Melhor framework?"
    assert data[0]['descricao'] == "Escolha um framework"






#pip install pytest flask-testing
#Executar os testes:
#pytest test_app.py
