import locale
from modulos import character, number , funcoes, PF, DadosPessoais, Documentos, PJ
import datetime as dt
import time

from modulos.PF import PFisica
from modulos.PJ import PJuridica

now = dt.datetime.now()
cf , cj = 0, 0
locale.setlocale(locale.LC_TIME,'Portuguese_Brazil.1252')

funcoes.animation('Inicializando...')

time.sleep(0.4)
print(now.strftime(f'Horário: %H:%M'))#hora

time.sleep(0.4)
user = character.character(f'Qual seu nome? ')

funcoes.separador()
time.sleep(0.4)
print(f'Olá {user}, vamos dar inicio aos cadastros da {now.strftime(f'%A dia %d/%m/%Y')}')
funcoes.separador()

time.sleep(0.4)
funcoes.title('Cadastro')

while True:
    print(f'{user}, qual cadastro deseja realizar?')
    print('Selecione a opção')
    print('[1] Pessoa Física ')
    print('[2] Pessoa Jurídica')
    print('[3] Sair do cadastro')

    op = number.num('Qual opção desejada? ')
    if op == 1:
        cf =  cf + 1
        funcoes.title(f'Pessoa Física')
        pFisica = PF.PFisica(nome = character.character('Nome: '), nasc = number.num('Ano de nascimento: '),
                             sexo = DadosPessoais.sexo('Sexo [M/F]: '),
                             endereco = character.character('Endereço: '), rg = Documentos.VRG('RG: '),
                             cpf = Documentos.VCPF('CPF: '), email = DadosPessoais.email('E-mail: '),
                             tel = DadosPessoais.tel('Digite o número de telefone incluindo DDD: '))
        pFisica.dados()
    elif op == 2:
        cj = cj + 1
        funcoes.title(f'Pessoa Jurídica')
        pJuridica = PJ.PJuridica(RazaoSocial = character.character('Razão Social: '), NomeFantasia = character.character('Nome Fantasia: '),
                                 cnpj = Documentos.VCNPJ('CNPJ: '),ie = Documentos.VIE('Inscrição Estadual: '),
                                 endereco = character.character('Endereço: '), tel = DadosPessoais.tel('Telefone: '),
                                 email = DadosPessoais.email('E-mail: '), site = DadosPessoais.site('Site: '),
                                 ResponsaveLegal = character.character('Responsável Legal: '),
                                 setor = character.character('Setor: '))
        pJuridica.dados()
    elif op == 3 :
        funcoes.separador()
        print('Agora vamos terminar os cadastros e descansar por hoje \o/')
        time.sleep(0.6)
        funcoes.separador()
        funcoes.PrintcomPausa(f'Foram contabilizados {cf} Pessoa Fisica e {cj} Pessoa Juridíca')
        break
    else:
        print(f'\033[31mDigite uma opção válida\033[m')
        continue