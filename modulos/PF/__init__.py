import datetime as dt
at = dt.datetime.now().year
from modulos import funcoes
import time

class PFisica:
    def __init__(self, nome, nasc,  sexo,  rg, cpf, endereco, email, tel ):
        self.nome = nome
        self.nasc = nasc
        self.idade = at - nasc
        self.sexo = sexo
        self.endereco = endereco
        self.rg = rg
        self.cpf = cpf
        self.email = email
        self.tel = tel

    def __str__(self):
        return  (f'Nome {self.nome}, Nascimento: {self.nasc}, Idade: {self.idade}, Sexo: {self.sexo}, Endereço {self.endereco}, '
                f'RG: {self.rg}, CPF: {self.cpf}, E-mail: {self.email}, Telefone: {self.tel}')

    def dados(self):
        #devolutiva de dados de pessoa fisica com temporizador e separador
        funcoes.title('Cadastro Finalizado')
        funcoes.PrintcomPausa(f'Nome: {self.nome}')
        funcoes.PrintcomPausa(f'Nasc: {self.nasc}')
        funcoes.PrintcomPausa(f'Idade: {self.idade}')
        funcoes.PrintcomPausa(f'Sexo: {'Masculino' if self.sexo.upper() == "M" else 'Feminino'}')
        funcoes.PrintcomPausa(f'Endereço: {self.endereco}')
        funcoes.PrintcomPausa(f'RG: {self.rg}')
        funcoes.PrintcomPausa(f'CPF: {self.cpf}')
        funcoes.PrintcomPausa(f'E-mail: {self.email}')
        funcoes.PrintcomPausa(f'Telefone: {self.tel}')
        time.sleep(0.6)
        funcoes.separador()