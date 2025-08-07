from modulos import funcoes
import datetime as dt
import time

now = dt.datetime.now().date()

class PJuridica:
    def __init__(self,  RazaoSocial, NomeFantasia, cnpj, ie, endereco, tel, email, ResponsaveLegal, site, setor):
        self.ID = funcoes.ID()
        self.Data = now.strftime('%d/%m/%Y')
        self.RazaoSocial = RazaoSocial
        self.NomeFantasia = NomeFantasia
        self.CNPJ = cnpj 
        self.IE = ie
        self.Endereco = endereco
        self.Tel = tel 
        self.Email = email
        self.Site = site
        self.ResponsaveLegal = ResponsaveLegal
        self.Setor = setor 
        
    def __str__(self):
        return (f'Razão Social {self.RazaoSocial},Nome Fantasia {self.NomeFantasia} ,CNPJ {self.cnpj} ,Inscrição Estadual {self.ie} ,'
                f'Endereço {self.endereco} ,Telefone {self.tel} ,Email {self.email} ,Site {self.site} ,Responsavel Legal {self.ResponsaveLegal} ,'
                f'Setor {self.setor}')

    def dados(self):
        #devolutiva dos dados de Pessoa juridicacom temporizador e separador
        funcoes.title('Cadastro Finalizado')
        funcoes.PrintcomPausa(f'ID: {self.ID}')
        funcoes.PrintcomPausa(f'Data {self.Data}')
        funcoes.PrintcomPausa(f'Razão Social: {self.RazaoSocial}')
        funcoes.PrintcomPausa(f'Nome Fantasia: {self.NomeFantasia}')
        funcoes.PrintcomPausa(f'CNPJ: {self.CNPJ}')
        funcoes.PrintcomPausa(f'Inscrição Estadual: {self.IE}')
        funcoes.PrintcomPausa(f'Endereço: {self.Endereco}')
        funcoes.PrintcomPausa(f'Telefone: {self.Tel}')
        funcoes.PrintcomPausa(f'E-mail: {self.Email}')
        funcoes.PrintcomPausa(f'Site: {self.Site}')
        funcoes.PrintcomPausa(f'Responsável Legal: {self.ResponsaveLegal}')
        funcoes.PrintcomPausa(f'Setor: {self.Setor}')
        time.sleep(0.6)
        funcoes.separador()