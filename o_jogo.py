import random
def cria_baralho():
    
    x = ['A♠','2♠','3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♥','2♥','3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♦','2♦','3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♣','2♣','3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
    
    
    return x

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
        return [3]
    elif extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 1]):
        return [1]
    elif indice > 2 and extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice - 3]):
        return [3]

    else:
        return []

def possui_movimentos_possiveis(x):
    if len(x)==1:
        return False
    
    i=0
    while i<len(x):
        if lista_movimentos_possiveis(x,i)==[1] or lista_movimentos_possiveis(x,i)==[3] or lista_movimentos_possiveis(x,i)==[1,3]:
            return True
        else:
            i+=1
        
    return False

def empilha(lista, origem, destino):
    if extrai_valor(lista[origem]) == extrai_valor(lista[destino]):
        lista[origem], lista[destino] = lista[destino], lista[origem]
        lista.remove(lista[origem])
    elif extrai_naipe(lista[origem]) == extrai_naipe(lista[destino]):
        lista[origem], lista[destino] = lista[destino], lista[origem]
        lista.remove(lista[origem])


    return lista


print("Paciência Acordeão") 
print("==================")

print("Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.")

x = input("você sabe jogar? (s/n) ")
if x == 'n':
    print("Existem apenas dois movimentos possíveis:")
    print("1. Empilhar uma carta sobre a carta imediatamente anterior;") 
    print("2. Empilhar uma carta sobre a terceira carta anterior.") 
    print("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:") 
    print("1. As duas cartas possuem o mesmo valor;")  
    print("2. As duas cartas possuem o mesmo naipe.") 
    print("Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.") 

else:
    print("Então boa sorte, vamos começar!")

baralho = cria_baralho()
random.shuffle(baralho)

x = input('Aperte ENTER para começar o jogo...')
if x == '':
    i=0
    while i<len(baralho):
        print('{0}. {1}'.format(i+1,baralho[i]))
        i+=1
    
    da_jogar=possui_movimentos_possiveis(baralho)
    while da_jogar:
        y = int(input('Escolha uma carta (digite um número entre 1 e {0}):'.format(len(baralho))))
        ag = True
        while ag:
            if y<1 or y>len(baralho):
                y=input('Posição inválida. Por favor escolha outra carta (digite um número entre 1 e {0}):'.format(len(baralho)))
            else:
                ag = False
        ag = True
        while ag:
            escolha = lista_movimentos_possiveis(baralho,y-1)
            if escolha==[1,3]:
                print('Sobre qual carta voce quer empilhar o {0}'.format(baralho[y-1]))
                print('1. {0}'.format(baralho[y-2]))
                print('2. {0}'.format(baralho[y-4]))
                a=input('Escolha 1 ou 2: ')
                ag1=True
                while ag1:
                    if a ==1:
                        empilha(baralho, y-1,y-2)
                        ag1=False
                    elif a==2:
                        empilha(baralho, y-1,y-4)
                        ag1=False
                    else:
                        a=input('Escolha 1 ou 2: ')
                ag=False
            elif escolha==[1]:
                empilha(baralho,y-1,y-2)
                ag=False
            elif escolha==[3]:
                empilha(baralho,y-1,y-4)
                ag=False
            else:
                input('A carta {0}, não pode ser movida. Por favor digite outro número (entre 1 e {1})'.format(baralho[y-1],len(baralho)))
            
        i=0
        while i<len(baralho):
            print('{0}. {1}'.format(i+1,baralho[i]))
            i+=1


