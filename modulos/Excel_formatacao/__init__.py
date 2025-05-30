from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table,TableStyleInfo

def ajuste(sheet):
    #ajuste 
    for col in sheet.iter_cols(min_row=1 ,max_row=sheet.max_row , min_col=1 ,max_col=sheet.max_column):
        max_length = 0 
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            if cell.value:
                max_length= max(max_length,len(str(cell.value)))
        sheet.column_dimensions[col_letter].width = max_length +6
        
def criar_tabela(sheet,nome_tabela):
    
    if nome_tabela in sheet.tables:
        del sheet.tables[nome_tabela]
    
    total_linhas = sheet.max_row
    total_colunas = sheet.max_column
    
    ultima_linha = get_column_letter(total_colunas)
    intervalo = f"A1:{ultima_linha}{total_linhas}"
    
    tabela = Table(displayName=nome_tabela, ref=intervalo)
    estilo = TableStyleInfo(
        name="TableStyleMedium9",
        showFirstColumn=False,
        showLastColumn=False,
        showRowStripes=True,
        showColumnStripes=False
    ) 
    tabela.tableStyleInfo = estilo
    
    sheet.add_table(tabela)
    
    print(f"Tabela {nome_tabela} criado com sucesso")