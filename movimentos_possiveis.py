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

def extrai_valor(y):
    x = str(y)
    carta = list(x)
    valor = []
    for i in carta:
        if i != '♦' and i != '♥' and i != '♣' and i != '♠':
            valor.append(i)

    valor_carta = ''.join(valor)

    return valor_carta

def lista_movimentos_possiveis(baralho,indice):
    if indice == 0:
        return []

    if extrai_valor(baralho[indice]) == extrai_valor(baralho[indice - 1]) and extrai_valor(baralho[indice]) == extrai_valor(baralho[indice - 3]):
        return [1,3]
    if extrai_valor(baralho[indice]) == extrai_valor(baralho[indice - 1]) and extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 3]):
        return [1,3]
    if extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 1]) and extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 3]):
        return [1,3]
    if extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 1]) and extrai_valor(baralho[indice]) == extrai_valor(baralho[indice - 3]):
        return [1,3]

    elif extrai_valor(baralho[indice]) == extrai_valor(baralho[indice - 1]):
        return [1]
    elif extrai_valor(baralho[indice]) == extrai_valor(baralho[indice - 3]):
        return [1]
    elif extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 1]):
        return [1]
    elif extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 3]):
        return [1]
    
    else:
        return []


#tentei com o metodo que vc sugeriu, mas ainda tem um errinho que nao descobri