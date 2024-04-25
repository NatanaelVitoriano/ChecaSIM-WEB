import requests
import os
from pathlib import Path
import json
import urllib
from lerArquivosSIM import dataNE, dataCO, dataLI, municipio

contratosNaoExistentes = []
licitacoesNaoExistentes = []

#Buscando na API
# try:
#     rLicitacao = requests.get('https://api-dados-abertos.tce.ce.gov.br/licitacoes?codigo_municipio=' + municipio + '&data_realizacao_autuacao_licitacao=2010-01-01_2030-12-31')
#     rContratos = requests.get('https://api-dados-abertos.tce.ce.gov.br/contrato?codigo_municipio=' + municipio + '&data_contrato=2010-01-01_2030-12-31&quantidade=0&deslocamento=0')
# except:
#     print("Tentando conexao com API TCE...")
#     try:
#         rLicitacao = requests.get('https://api-dados-abertos.tce.ce.gov.br/licitacoes?codigo_municipio=' + municipio + '&data_realizacao_autuacao_licitacao=2010-01-01_2030-12-31')
#         rContratos = requests.get('https://api-dados-abertos.tce.ce.gov.br/contrato?codigo_municipio=' + municipio + '&data_contrato=2010-01-01_2030-12-31&quantidade=0&deslocamento=0')
#     except:
#         print("Não foi possivel conectar-se a API.")
#         os.system("PAUSE")
#         quit()
        
# json = rLicitacao.json()
# listaDeLicitacoes = json['data']

# json = rContratos.json()
# listaDeContratos = json['data']

#Buscando json local
with open('C:/Users/Supor/Documents/python/Teste Arquivos SIM/arquivos/contratos.json') as arquivo:
    dados = json.load(arquivo)
listaDeContratos = dados['data']

with open('C:/Users/Supor/Documents/python/Teste Arquivos SIM/arquivos/licitacoes.json') as arquivo:
    dados = json.load(arquivo)
listaDeLicitacoes = dados['data']

#Checando contrato
for x, data in enumerate(dataNE, start=1):
    if data[24].replace('"',"") == "":
        continue
    
    contratoNoSIM = False
    contratoNoArquivoCO = False
    
    while True:
        #Checando API
        for i, contrato in enumerate(listaDeContratos, start=0):
            if data[24].replace('"',"") == contrato['numero_contrato'] and data[25].replace('"',"") == contrato['data_contrato'].replace("-","")[0:8]:
                contratoNoSIM = True
            for i, contratoCO in enumerate(dataCO, start=0):
                if data[24].replace('"',"") == contratoCO[3].replace('"',"") and data[25].replace('"',"") == contratoCO[4].replace('"',""):
                    contratoNoArquivoCO = True
                    break
                    
        if contratoNoSIM and contratoNoArquivoCO:
            print("Contrato " + data[24].replace('"',"") + " na linha " + str(x) + " do arquivo NE está duplicado.")
            
        elif contratoNoSIM and contratoNoArquivoCO == False:
            print("Contrato " + data[24].replace('"',"") + " na linha " + str(x) + " do arquivo NE não esta no arquivo CO")
        
        elif contratoNoSIM == False and contratoNoArquivoCO == False:
            print("Contrato " + data[24].replace('"',"") + " na linha " + str(x) + " invalido no arquivo CO.")
            
        elif contratoNoSIM == False and contratoNoArquivoCO == True:
            print("Contrato " + data[24].replace('"',"") + " OK.")
            
        break
        
# Checando Licitacao

for x, ctCO in enumerate(dataCO, start= 1):
    if ctCO[20].replace('"',"") == "":
        continue
    licitacaoNoSIM = False
    licitacaoNoArquivoLI = False
    while True:
        
        for licitacao in listaDeLicitacoes:
            if ctCO[20].replace('"',"") == licitacao['numero_licitacao'] and ctCO[19] == licitacao["data_realizacao_autuacao_licitacao"].replace('"',"").replace("-",""):
                licitacaoNoSIM = True
                break
            
        for licitacaoLI in dataLI:
            if ctCO[20].replace('"',"") == licitacaoLI[3].replace('"',"") and ctCO[19] == licitacaoLI[2]:
                licitacaoNoArquivoLI = True
                break
            
        if licitacaoNoSIM and licitacaoNoArquivoLI:
            print("Licitacao " + ctCO[20].replace('"',"") + " na linha " + str(x) + " do arquivo LI está duplicada.")
            
        elif licitacaoNoSIM == False and licitacaoNoArquivoLI:
            print("Linha ok")
            
        elif licitacaoNoSIM == False and licitacaoNoArquivoLI == False:
            print("Licitacao " + ctCO[20].replace('"',"") + " na linha " + str(x) +  " do arquivo CO está invalida. Não consta na API nem no LI")
        
        else:
            break
        
        break

os.system("PAUSE")