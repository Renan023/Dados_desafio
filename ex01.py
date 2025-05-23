import pandas as pd

dados = [{"Nome": "Renan", "Idade": 30}]

df = pd.DataFrame(dados)
df.to_excel("cadastro.xlsx", index=False)

print("Excel criado com sucesso.")
