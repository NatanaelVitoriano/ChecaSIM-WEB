import requests
import os
from pathlib import Path
import json
from lerArquivosSIM import dataNE, dataCO, dataLI, municipio

licitacoesEmpenhadas = []
listaDeLicitacoesNoLI = []
listaDeLicitacoesNoSIMWEB = []

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "arquivos/"
caminho = os.path.join(script_dir, rel_path)
pathLote = Path(caminho)

with open(caminho + 'contratos.json', encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
listaDeContratos = dados['data']

with open(caminho + 'licitacoes.json', encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
listaDeLicitacoes = dados['data']

#Checando licitacao
for licitacaoLI in dataLI:
    listaDeLicitacoesNoSIMWEB.append([licitacaoLI[3].replace('"',""),licitacaoLI[2]])

for licitacao in listaDeLicitacoes:
    listaDeLicitacoesNoSIMWEB.append([licitacao['numero_licitacao'].replace('"',""), licitacao["data_realizacao_autuacao_licitacao"].replace('"',"").replace("-","")])

licitacaoFaltando = True   
for x, data in enumerate(dataNE, start=1):
    if data[24].replace('"', '') == "":
        continue

    licitacaoFaltando = True 
    for i in listaDeLicitacoesNoSIMWEB:
        if data[26].replace('"',"") == i[0] and data[27].replace('"',"") == i[1]:
            licitacaoFaltando = False 
            break
    
    if licitacaoFaltando:
        print(f"Licitação faltando para a linha NE {x}: {data[26]}")
        
for licitacaoLI in dataLI:
    for licitacao in listaDeLicitacoes:
        if licitacaoLI[3].replace('"',"") == licitacao['numero_licitacao']:
            print("Licitacao " + licitacaoLI[3] + " duplicada")
            

for x, ctCO in enumerate(dataCO, start= 1):
    if ctCO[20].replace('"',"") == "":
        continue
    
    licitacaoNoSIM = False
    licitacaoNoArquivoLI = False
    while True:
        for licitacaoApi in listaDeLicitacoes:
            if ctCO[20].replace('"',"") == licitacaoApi['numero_licitacao'].replace('"',"") and ctCO[19] == licitacaoApi["data_realizacao_autuacao_licitacao"].replace('"',"").replace("-",""):
                licitacaoNoSIM = True
                break
            
        for licitacaoLI in dataLI:
            if ctCO[20].replace('"',"") == licitacaoLI[3].replace('"',"") and ctCO[19] == licitacaoLI[2]:
                
                licitacaoNoArquivoLI = True
                break
            
        if licitacaoNoSIM and licitacaoNoArquivoLI:
            print("Licitacao " + ctCO[20] + " na linha " + str(x) + " do arquivo CO está duplicada. Está indo novamente no arquivo LI")
            
        elif licitacaoNoSIM == False and licitacaoNoArquivoLI == False:
            print("Licitacao " + ctCO[20] + " na linha " + str(x) +  " do arquivo CO sem empenho")
        
        else:
            break

        break

#Checando contratos
for x, dadosCO in enumerate(dataNE, start=1):
    if dadosCO[24].replace('"', '') == "":
        continue
    
    contratoNoSIM = False
    contratoNoArquivoCO = False
    dataDiferente = False
    while True:
        for i, contrato in enumerate(listaDeContratos, start=0):
            if dadosCO[24].replace('"',"") == contrato['numero_contrato'].replace('"',"") and dadosCO[25].replace('"',"") == contrato['data_contrato'].replace("-","")[0:8]:
                contratoNoSIM = True
                
            elif dadosCO[24].replace('"',"") == contrato['numero_contrato'].replace('"',"") and dadosCO[25].replace('"',"") != contrato['data_contrato'].replace("-","")[0:8]:
                print("Contrato " + dadosCO[24] + " com data diferente")
                
        for i, contratoCO in enumerate(dataCO, start=0):
                
                if dadosCO[24].replace('"',"") == contratoCO[3].replace('"',"") and dadosCO[25].replace('"',"") == contratoCO[4].replace('"',""):
                    contratoNoArquivoCO = True
                    break
                
        if contratoNoSIM and contratoNoArquivoCO:
            print("Contrato " + dadosCO[24].replace('"',"") + " na linha " + str(x) + " do arquivo NE está duplicado.")
            
        elif contratoNoSIM and contratoNoArquivoCO == False:
            pass
                
        elif contratoNoSIM == False and contratoNoArquivoCO == False:
            print("Contrato " + dadosCO[24].replace('"',"") + " na linha " + str(x) + " invalido no arquivo CO.")
            
        elif contratoNoSIM == False and contratoNoArquivoCO == True:
            pass
        
        break