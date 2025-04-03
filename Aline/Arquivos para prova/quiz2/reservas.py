#criar classe para organização do código


class SistemaReservas:
    # Inicializador da classe - roda quando criamos uma nova instância
    def __init__(self):
        # Lista para armazenar todos os voos disponíveis
        self.voos_disponiveis = []  
        # Lista para armazenar todas as reservas feitas
        self.reservas = []          
    
    # Método para adicionar novos voos
    def adicionar_voo(self, voo):
        # Adiciona um dicionário de voo à lista de voos disponíveis
        self.voos_disponiveis.append(voo)  
    
    # Método para pesquisar voos por origem/destino
    def pesquisar_voos(self, origem, destino):
        # List comprehension: filtra os voos onde origem e destino batem
        return [v for v in self.voos_disponiveis 
                if v['origem'] == origem and v['destino'] == destino]
    
    # Método para reservar um voo específico
    def reservar_voo(self, id_voo, nome_passageiro):
        # Procura o voo pelo ID (next retorna o primeiro que encontrar)
        # Se não encontrar, retorna None
        voo = next((v for v in self.voos_disponiveis if v['id'] == id_voo), None)
        
        if voo:  # Se encontrou o voo
            # Cria um dicionário com os dados da reserva
            reserva = {
                'id': len(self.reservas)+1,  # ID baseado no tamanho atual
                'voo': voo,                  # Referência ao voo completo
                'passageiro': nome_passageiro # Nome do passageiro
            }
            # Adiciona a reserva à lista
            self.reservas.append(reserva)  
            return reserva
        return None  # Retorna None se não encontrou o voo
    
    # Método para cancelar reserva
    def cancelar_reserva(self, id_reserva):
        # Filtra a lista de reservas, mantendo só as com ID diferente
        self.reservas = [r for r in self.reservas if r['id'] != id_reserva]  