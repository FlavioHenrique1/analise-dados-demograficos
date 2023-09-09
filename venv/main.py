import pandas as pd
import json

# Carregue a planilha em um DataFrame do pandas
df = pd.read_excel("lista_país.xlsx")

# Converta o DataFrame para um dicionário
dados_json = df.to_dict(orient='records')

# Salve o dicionário como um arquivo JSON no mesmo local da planilha
with open("dados.json", "w") as arquivo_json:
    json.dump(dados_json, arquivo_json)

print("Dados foram convertidos para JSON e o arquivo 'dados.json' foi salvo.")

# Abra o arquivo JSON
with open("dados.json", "r") as arquivo_json:
    dados_objeto = json.load(arquivo_json)

# Agora, 'dados_objeto' conterá o conteúdo do arquivo JSON como um objeto Python
# print(dados_objeto)


# Converter os valores da estimativa da ONU em números inteiros
for país in dados_objeto:
    estimativa_onu = país['Estimativa da ONU'].replace(' ', '')  # Remover espaços
    país['Estimativa da ONU'] = int(estimativa_onu)

# Calcular a população mundial (soma das estimativas da ONU)
população_mundial = sum(país['Estimativa da ONU'] for país in dados_objeto)

# Calcular o percentual da estimativa da ONU para cada país e adicioná-lo ao JSON
for país in dados_objeto:
    percentual_onu = (país['Estimativa da ONU'] / população_mundial) * 100
    país['Percentual da ONU'] = round(percentual_onu, 2)

with open('dados_atualizados.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados_objeto, arquivo_json, ensure_ascii=False, indent=4)