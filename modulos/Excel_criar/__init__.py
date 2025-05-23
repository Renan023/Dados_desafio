import os 
from openpyxl import Workbook

def Excel_vazio(nome_arquivo):
    
    if not os.path.exists(nome_arquivo):
        wb = Workbook()

        wb.save(nome_arquivo)
        
        print(f"{nome_arquivo} criado com sucesso")
    else:
        print(f"{nome_arquivo} já existente")

