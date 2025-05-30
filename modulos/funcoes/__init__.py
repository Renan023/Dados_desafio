import time
import os

def title(msg):
    #exibe título centralizao com uma linnha superior e inferior
    print('='*100)
    print(msg.center(100))
    print('='*100)

def animation(animation):
    #exibe animação como se estivesse escrevendo uma determinada palavra
    word = (animation)

    for letra in word:
        print(letra, end="", flush=True)
        time.sleep(0.2)

    print()

def separador():
    print('-'*100)

def PrintcomPausa(texto,pausa=0.3):
    #exibe um determinado print com uma pausa em que o se escolhe o temporizador
    print(texto)
    time.sleep(pausa)

def ID(caminho = 'id.txt'):
    #aqui se cria ou le o último ID e incrementa
    if os.path.exists(caminho):
        with open(caminho,'r',) as arquivo:
            end_a = int(arquivo.read())
    else:
        end_a = 0

    new_a = end_a + 1

    with open(caminho , 'w', ) as arquivo :
        arquivo.write(str(new_a))

    return new_a