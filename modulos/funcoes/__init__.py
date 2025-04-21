import time

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