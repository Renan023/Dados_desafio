from openpyxl.utils import get_column_letter

def ajuste(planilha):
    #ajuste 
    for col in planilha.iter_cols(min_row=1 ,max_row=planilha.max_row , min_col=1 ,max_col=planilha.max_column):
        max_length = 0 
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            if cell.value:
                max_length= max(max_length,len(str(cell.value)))
        planilha.column_dimensions[col_letter].width = max_length +2