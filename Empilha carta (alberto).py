def extrai_valor(y):
    x = str(y)
    carta = list(x)
    valor = []
    for i in carta:
        if i != '♦' and i != '♥' and i != '♣' and i != '♠':
            valor.append(i)

    valor_carta = ''.join(valor)

    return valor_carta

def extrai_naipe(y):
    x = str(y)
    carta = list(x)
    for i in carta:
        if i == '♦':
            return '♦'
        elif i == '♥':
            return '♥'
        elif i == '♣':
            return '♣'
        elif i == '♠':
            return '♠'

def lista_movimentos_possiveis(baralho,indice):
    if indice == 0:
        return []

    if indice > 2 and extrai_valor(baralho[indice]) == extrai_valor(baralho[indice - 1]) and extrai_valor(baralho[indice]) == extrai_valor(baralho[indice - 3]):
        return [1,3]
    if indice > 2 and extrai_valor(baralho[indice]) == extrai_valor(baralho[indice - 1]) and extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 3]):
        return [1,3]
    if indice > 2 and extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 1]) and extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 3]):
        return [1,3]
    if indice > 2 and extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 1]) and extrai_valor(baralho[indice]) == extrai_valor(baralho[indice - 3]):
        return [1,3]

    elif extrai_valor(baralho[indice]) == extrai_valor(baralho[indice - 1]):
        return [1]
    elif indice > 2 and extrai_valor(baralho[indice]) == extrai_valor(baralho[indice - 3]):
        return [1]
    elif extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 1]):
        return [1]
    elif indice > 2 and extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 3]):
        return [1]

    else:
        return []

def empilha(x, origem, destino):
    if lista_movimentos_possiveis(x,origem) == []:
        return x
    if lista_movimentos_possiveis(x,origem) == [1] and destino ==1:
        x[origem], x[destino] = x[destino], x[origem]
        x.remove(x[origem])
        return x
    if  lista_movimentos_possiveis(x,origem) == [3] and destino==3:
        x[origem], x[destino] = x[destino], x[origem]
        x.remove(x[origem])
        return x
    elif lista_movimentos_possiveis(x,origem) == [1,3] and destino==1:
        x[origem], x[destino] = x[destino], x[origem]
        x.remove(x[origem])
        return x 
    elif lista_movimentos_possiveis(x,origem) == [1,3] and destino==3:
        x[origem], x[destino] = x[destino], x[origem]
        x.remove(x[origem])
        return x