import pytest
# Importa a classe que vamos testar
from reservas import SistemaReservas  

# Fixture - prepara dados de teste que serão reutilizados
@pytest.fixture
def sistema():
    # Cria uma instância do sistema
    sist = SistemaReservas()  
    # Adiciona voo de exemplo (SP-RJ)
    sist.adicionar_voo({'id': 1, 'origem': 'SP', 'destino': 'RJ'})  
    # Adiciona voo de exemplo (RJ-BA)
    sist.adicionar_voo({'id': 2, 'origem': 'RJ', 'destino': 'BA'})   
    return sist  # Retorna o sistema configurado

# Teste para pesquisa de voos
def test_pesquisa_voos(sistema):
    # Verifica se encontrou 1 voo SP-RJ
    assert len(sistema.pesquisar_voos('SP', 'RJ')) == 1  
    # Verifica se não encontrou voos RJ-SP
    assert len(sistema.pesquisar_voos('RJ', 'SP')) == 0  

# Teste para reserva válida
def test_reserva_valida(sistema):
    # Tenta reservar o voo ID 1
    reserva = sistema.reservar_voo(1, "João Silva")  
    # Verifica se a reserva foi criada
    assert reserva is not None  
    # Verifica se a lista de reservas tem 1 item
    assert len(sistema.reservas) == 1  

# Teste para reserva inválida
def test_reserva_invalida(sistema):
    # Tenta reservar voo que não existe (ID 999)
    assert sistema.reservar_voo(999, "Maria") is None  

# Teste para cancelamento
def test_cancelamento(sistema):
    # Faz uma reserva
    reserva = sistema.reservar_voo(1, "Ana")  
    # Cancela a reserva
    sistema.cancelar_reserva(reserva['id'])  
    # Verifica se a lista de reservas está vazia
    assert len(sistema.reservas) == 0  