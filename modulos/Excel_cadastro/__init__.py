#transforma a listade dicionários em tabelas
import pandas as pd
#verifica se um arquivo já existe
import os

#cria o arquivo e se já existe ele atualiza
def cadastro_excel(lista_pf, lista_pj , nome_arquivo = 'cadastro.xlsx'):
    if os.path.exists(nome_arquivo):
        writer = pd.ExcelWriter(nome_arquivo, engine = 'openpyxl', mode ='a', if_sheet_exists='overlay')
    else:
        writer = pd.ExcelWriter(nome_arquivo, engine = 'openpyxl')
        print(f'Arquivo {nome_arquivo} criado com sucesso!!')

    #escreve ou atualiza o cadastro de Pessoa Fisica
    if lista_pf:
        df_pf = pd.DataFrame(lista_pf)
        if 'Pessoa Física' in writer.book.sheetnames:
            start_row = writer.book['Pessoa Física'].max_row
        else:
            start_row = 0
        df_pf.to_excel(writer,sheet_name='Pessoa Física', index= False,header = (start_row == 0), startrow= start_row)

    #escreve ou atualiza o cadastro de Pessoa Juridica
    if lista_pj:
        df_pj = pd.DataFrame(lista_pj)
        if 'Pessoa Juridica' in writer.book.sheetnames:
            start_row = writer.book['Pessoa Juridica'].max_row
        else:
            start_row = 0
        df_pj.to_excel(writer, sheet_name ='Pessoa Juridica',  index = False, header = (start_row == 0), startrow= start_row)

    #fecha o arquivo
    writer.close()
    print(f'Arquivo {nome_arquivo} atualizado com sucesso ')