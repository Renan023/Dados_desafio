from modulos import character

def VRG(rg):
    #validador para RG
    while True:
        try:
            rg = character.character(rg).strip().replace('.','').replace('-','').upper()

            if not rg.isalnum() or not (7<= len(rg) <= 9):
                print('\033[31mDigite um RG válido\033[m')
                continue
        except KeyboardInterrupt:
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return rg

def VCPF(cpf):
    #validador para CPF
    while True:
        try:
            cpf = character.character(cpf).strip().replace('.','').replace('-','')

            if not cpf.isdigit() or len(cpf) != 11:
                print('\033[31mDigite um CPF válido\033[m')
                continue
        except KeyboardInterrupt:
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return cpf

def VCNPJ(cnpj):
    #validador para CNPJ
    while True:
        try:
            cnpj = character.character(cnpj).strip().replace('/','').replace('.','').replace('-','')
            if not cnpj.isdigit() or len(cnpj) != 14 :
                print('\033[31mDigite um CNPJ válido\033[m')
                continue
        except KeyboardInterrupt:
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return cnpj

def VIE(ie):
    #validador de inscrição estadual
    while True:
        try:
            ie = character.character(ie).strip().replace('.','').replace('-','')
            if ie.lower() == 'isento':
                return 'ISENTO'
            if ie.isdigit() or len(ie) > 9 and len(ie) < 15:
                print('\033[31mDigite uma IE válida\033[m')
                continue
        except KeyboardInterrupt:
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return ie