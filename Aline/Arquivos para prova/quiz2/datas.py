from datetime import datetime # Importa a função datetime para trabalhar com datas

def diferenca_datas(data1, data2, unidade='dias'):
    diff = data2 - data1
    # diff será um objeto (local onde será armazenado) 'timedelta' que guarda: dias, segundos e microssegundos

    if unidade == 'dias':
        return diff.days # Acessa o atributo .days do timedelta (já vem calculado)
    
    elif unidade == 'horas':
        return diff.days * 24 + diff.seconds // 3600
        # diff.days * 24 -> transforma dias em horas (9 dias = 216 horas)
        # diff.seconds // 3600 -> converte segundos para horas (3600 segundos = 1 hora)
    
    elif unidade == 'minutos':
        return diff.days * 1440 + diff.seconds // 60
        # diff.days * 1440 -> dias para minutos (1 dia = 1440 minutos)
        # diff.seconds // 60 -> segundos para minutos (60 segundos = 1 minuto)
    
    elif unidade == 'anos':
        return diff.days // 365
        # Cálculo aproximado (divisão inteira por 365)
    
    else:
        return diff
        # Se a unidade não for reconhecida, retorna o objeto diff completo