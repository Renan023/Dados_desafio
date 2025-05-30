from modulos import character

def sexo(sexo):
    #validação para sexo masculino ou feminino
    while True:
        try:
            sexo = character.character(sexo).strip().upper()[0]
            if sexo not in 'MmFf':
                print('\033[31mDigite uma informação aceita\033[m')
                continue
        except(KeyboardInterrupt):
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return sexo
        
def email(email):
    #validação para email
    while True:
        try:
            email = character.character(email).strip().lower()
            if '@' not in email or '.' not in email :
                print('\033[31mDigite um e-mail válido\033[m')
                continue
            if email.startswith('@') or email.endswith('@') :
                print('\033[31mDigite um e-mail válido\033[m')
                continue
        except KeyboardInterrupt:
            print('\033[31mInterrompkido pelo  usuário')
            break
        else:
            return email

def tel(tel):
    #validação para telefone
    while True:
        try:
            tel = character.character(tel).strip()
            if not tel.isdigit() or len(tel) not in [10,11]:
                print('\033[31mDigite um número de telefone válido\033[m')
                continue
        except KeyboardInterrupt:
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return tel

def site(site):
    #validação para site
    while True:
        try:
            site = character.character(site).strip().lower()
            if not (site.startswith('http://') or site.startswith('https://')):
                print('\033[31mDigite um site válido\033[m')
                continue
        except KeyboardInterrupt:
            print('\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return site