import datetime as dt
from modulos import funcoes
import time

at = dt.datetime.now().year
now = dt.datetime.now().date()

class PFisica:
    def __init__(self, nome, nasc,  sexo,  rg, cpf, endereco, email, tel ):
        self.ID = funcoes.ID()
        self.Data = now.strftime('%d/%m/%Y')
        self.Nome = nome
        self.Nasc = nasc
        self.Idade = at - nasc
        self.Sexo = sexo
        self.Endereco = endereco
        self.RG = rg
        self.CPF = cpf
        self.Email = email
        self.Tel = tel

    def __str__(self):
        return  (f'Nome {self.nome}, Nascimento: {self.nasc}, Idade: {self.idade}, Sexo: {self.sexo}, Endereço {self.endereco}, '
                f'RG: {self.rg}, CPF: {self.cpf}, E-mail: {self.email}, Telefone: {self.tel}')

    def dados(self):
        #devolutiva de dados de pessoa fisica com temporizador e separador
        funcoes.title('Cadastro Finalizado')
        funcoes.PrintcomPausa(f'ID: {self.ID}')
        funcoes.PrintcomPausa(f'Data: {self.Data}')
        funcoes.PrintcomPausa(f'Nome: {self.Nome}')
        funcoes.PrintcomPausa(f'Nasc: {self.Nasc}')
        funcoes.PrintcomPausa(f'Idade: {self.Idade}')
        funcoes.PrintcomPausa(f"Sexo: {'Masculino' if self.Sexo.upper() == 'M' else 'Feminino'}")
        funcoes.PrintcomPausa(f'Endereço: {self.Endereco}')
        funcoes.PrintcomPausa(f'RG: {self.RG}')
        funcoes.PrintcomPausa(f'CPF: {self.CPF}')
        funcoes.PrintcomPausa(f'E-mail: {self.Email}')
        funcoes.PrintcomPausa(f'Telefone: {self.Tel}')
        time.sleep(0.6)
        funcoes.separador()