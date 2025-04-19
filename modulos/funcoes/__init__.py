import time

def title(msg):

    print('='*100)
    print(msg.center(100))
    print('='*100)

def animation(animation):

    word = (animation)

    for letra in word:
        print(letra, end="", flush=True)
        time.sleep(0.2)

    print()

def separador():
    print('-'*100)

def PrintcomPausa(texto,pausa=0.3):
    print(texto)
    time.sleep(pausa)