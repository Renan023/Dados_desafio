def adicionar_formula(sheet, celula,formula):
    
    try: 
        sheet[celula] = formula
        print(f"Fórmula {formula} adicionada com sucesso em {celula} ")
        
    except Exception as e:
        print(f"Fórmula não foi adicionada em {celula} : {e}")