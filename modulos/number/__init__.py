def num(n):
    #validador para números
    while True:
        try:
            num = int(input(n))
        except(ValueError, KeyError):
            print(f'\033[31mDigite um valor válido\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return num



