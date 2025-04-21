import pandas as pd

def exportExcel(lista_pf, lista_pj, nome_arquivo ='cadastro.xlsx' ):

    with pd.ExcelWriter(nome_arquivo , engine = 'openpyxl')as writer:
        if lista_pf:
            df_pf = pd.DataFrame(lista_pf)
            df_pf.to_excel(writer, sheet_name = 'Pessoa Física', index = False)

        if lista_pj:
            df_pj = pd.DataFrame(lista_pj)
            df_pj.to_excel(writer,sheet_name = 'Pessoa Juridica', index = False)

    print(f'Arquivo {nome_arquivo} gerado com sucesso ')