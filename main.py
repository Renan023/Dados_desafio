#importação do locale para a configuração regional
import locale
#módulos importados devidamente separados para a organizaçao do código
from modulos import character, number , funcoes, PF, DadosPessoais, Documentos, PJ, Excel
#importação para ajustar a data
import datetime as dt
#importação para colocar como temporizador
import time

#listas vazias para armazenar cadastro de PF e PJ
cadastro_PF , cadastro_PJ = [] , []
#armazena o tempo de agora
now = dt.datetime.now()
#inicializador dos contadores
cf , cj = 0, 0
#configuração regional no caso o Brasil em português, com suas devidas formatações conforme padrão brassileiro
locale.setlocale(locale.LC_TIME,'Portuguese_Brazil.1252')


funcoes.animation('Inicializando...')

time.sleep(0.4)
#hora
print(now.strftime(f'Horário: %H:%M'))

time.sleep(0.4)
#pergunta o nome do usuário
user = character.character(f'Qual seu nome? ')

funcoes.separador()
time.sleep(0.4)
#saudação com o dia da semana e dia, mês e ano
print(f'Olá {user}, vamos dar inicio aos cadastros da {now.strftime(f'%A dia %d/%m/%Y')}')
funcoes.separador()

time.sleep(0.4)
funcoes.title('Cadastro')

#aqui entra em loop infinito em que pergunto parao usuário, qual ele opção ele deseja selecionar 1, 2 ou 3
#se não for nenhuma dessas opções entra em loop pedindo uma informação válida especifíca
while True:
    print(f'{user}, qual cadastro deseja realizar?')
    print('Selecione a opção')
    print('[1] Pessoa Física ')
    print('[2] Pessoa Jurídica')
    print('[3] Sair do cadastro')

    op = number.num('Qual opção desejada? ')
    if op == 1:
        #contabiliza  o cadastro de pessoa física
        cf += 1
        funcoes.title(f'Pessoa Física')
        #cadastro de pessoa física com seus devidos módulos e validações
        pFisica = PF.PFisica(nome = character.character('Nome: '), nasc = number.num('Ano de nascimento: '),
                             sexo = DadosPessoais.sexo('Sexo [M/F]: '),
                             endereco = character.character('Endereço: '), rg = Documentos.VRG('RG: '),
                             cpf = Documentos.VCPF('CPF: '), email = DadosPessoais.email('E-mail: '),
                             tel = DadosPessoais.tel('Digite o número de telefone incluindo DDD: '))
        #devolutiva do cadastro
        pFisica.dados()
        #guarda em dicionários e copia os cadastros de pessoa fisica
        cadastro_PF.append(pFisica.__dict__.copy())
    elif op == 2:
        #contabiliza a pessoa juridica
        cj += 1
        funcoes.title(f'Pessoa Jurídica')
        #cadastro de pessoa juridíca com seus devidos módulos e validação
        pJuridica = PJ.PJuridica(RazaoSocial = character.character('Razão Social: '), NomeFantasia = character.character('Nome Fantasia: '),
                                 cnpj = Documentos.VCNPJ('CNPJ: '),ie = Documentos.VIE('Inscrição Estadual: '),
                                 endereco = character.character('Endereço: '), tel = DadosPessoais.tel('Telefone: '),
                                 email = DadosPessoais.email('E-mail: '), site = DadosPessoais.site('Site: '),
                                 ResponsaveLegal = character.character('Responsável Legal: '),
                                 setor = character.character('Setor: '))
        #devolutiva do cadastro de pessoa juridica
        pJuridica.dados()
        #guarda em dicionários e copia os cadastros de pessoa juridica
        cadastro_PJ.append(pJuridica.__dict__.copy())
    elif op == 3 :
        funcoes.separador()
        print('Agora vamos terminar os cadastros e descansar por hoje \o/')
        time.sleep(0.6)
        funcoes.separador()
        #mostra quantos foram cadastrados tanto de pessoa fisica como juridica
        funcoes.PrintcomPausa(f'Foram contabilizados {cf} Pessoa Fisica e {cj} Pessoa Juridíca')
        #Exporto para o excel antes de sair
        Excel.exportExcel(cadastro_PF, cadastro_PJ)
        #encerra o loop
        break
    else:
        print(f'\033[31mDigite uma opção válida\033[m')
        #continua o loop até a opçao correta ser digitada
        continue