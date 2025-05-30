from modulos import funcoes
import datetime as dt
import time

now = dt.datetime.now()

class PJuridica:
    def __init__(self,  RazaoSocial, NomeFantasia, cnpj, ie, endereco, tel, email, ResponsaveLegal, site, setor):
        self.id = funcoes.ID()
        self.data = now
        self.RazaoSocial = RazaoSocial
        self.NomeFantasia = NomeFantasia
        self.cnpj = cnpj 
        self.ie = ie
        self.endereco = endereco
        self.tel = tel 
        self.email = email
        self.site = site
        self.ResponsaveLegal = ResponsaveLegal
        self.setor = setor 
        
    def __str__(self):
        return (f'Razão Social {self.RazaoSocial},Nome Fantasia {self.NomeFantasia} ,CNPJ {self.cnpj} ,Inscrição Estadual {self.ie} ,'
                f'Endereço {self.endereco} ,Telefone {self.tel} ,Email {self.email} ,Site {self.site} ,Responsavel Legal {self.ResponsaveLegal} ,'
                f'Setor {self.setor}')

    def dados(self):
        #devolutiva dos dados de Pessoa juridicacom temporizador e separador
        funcoes.title('Cadastro Finalizado')
        funcoes.PrintcomPausa(f'ID: {self.id}')
        funcoes.PrintcomPausa(f'Data {self.data}')
        funcoes.PrintcomPausa(f'Razão Social: {self.RazaoSocial}')
        funcoes.PrintcomPausa(f'Nome Fantasia: {self.NomeFantasia}')
        funcoes.PrintcomPausa(f'CNPJ: {self.cnpj}')
        funcoes.PrintcomPausa(f'Inscrição Estadual: {self.ie}')
        funcoes.PrintcomPausa(f'Endereço: {self.endereco}')
        funcoes.PrintcomPausa(f'Telefone: {self.tel}')
        funcoes.PrintcomPausa(f'E-mail: {self.email}')
        funcoes.PrintcomPausa(f'Site: {self.site}')
        funcoes.PrintcomPausa(f'Responsável Legal: {self.ResponsaveLegal}')
        funcoes.PrintcomPausa(f'Setor: {self.setor}')
        time.sleep(0.6)
        funcoes.separador()