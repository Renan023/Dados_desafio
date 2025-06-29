import os 

def Excel_existente():
    
    arquivos = [arq for arq in os.listdir() if arq.endswith(('.xlsx','xlsm'))]
    print('Arquivo encontrado')
    
    if not arquivos:
        
        print('\033[31mNenhum arquivo encontrado\033[m')
        return None
    
    arquivos.sort(key=os.path.getmtime,reverse=True)
    return arquivos[0]