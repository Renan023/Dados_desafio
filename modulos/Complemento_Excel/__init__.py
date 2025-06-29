from modulos.Excel_formatacao import ajuste, alinhar, bordas, congelar_cabecalho, criar_tabela, Copiar,cabecalho
from openpyxl import load_workbook

def complementos(nome_arquivo, origem, aba_destino,nome_tabela,background,font):
    
    Copiar(nome_arquivo,origem,aba_destino)
    
    wb = load_workbook(nome_arquivo)
    aba = wb[aba_destino]
    
    ajuste(aba)
    alinhar(aba)
    bordas(aba)
    cabecalho(aba,background,font)
    congelar_cabecalho(aba)
    criar_tabela(aba,nome_tabela)
    
    wb.save(nome_arquivo)
    
    print("Funções complementares adicionadas com sucesso") 
    