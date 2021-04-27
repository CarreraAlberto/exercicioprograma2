def extrai_valor(y):
    x = str(y)
    carta = list(x)
    valor = []
    for i in carta:
        if i != '♦' and i != '♥' and i != '♣' and i != '♠':
            valor.append(i)

    valor_carta = ''.join(valor)

    return valor_carta