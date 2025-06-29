def character(char):
    #validaçao para caracteres somente
    while True:
        try:
            char = input(char).capitalize()
            if not char:
                print(f'\033[31mDigite uma informação válida\033[m')
                continue
        except(KeyboardInterrupt):
            print(f'\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return char

def question(resp):
    #validação para questões de sim ou não
    while True:
        try:
            resp = character(resp).strip().upper()[0]
            if resp not in 'SN':
                print(f'\033[31mDigite uma informação válida\033[m')
                continue
        except(KeyboardInterrupt):
            print(f'\033[31mInterrompido pelo usúario\033[m')
            break
        else:
            return resp
