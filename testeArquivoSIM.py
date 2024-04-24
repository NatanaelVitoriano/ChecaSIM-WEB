import requests
import os
from pathlib import Path
import urllib
import json
from lerArquivosSIM import dataNE, dataCO, dataLI

# codigoDoMunicipio = '054'
# myurl = 'https://api-dados-abertos.tce.ce.gov.br/licitacoes?codigo_municipio=' + codigoDoMunicipio + '&data_realizacao_autuacao_licitacao=2010-01-01_2023-12-31'
# print("Informe o numero do municipio: ")
# codigoDoMunicipio = str(input())

# try:
#     rContratos = requests.get(myurl)
#     # rLicitacao = requests.get('https://api-dados-abertos.tce.ce.gov.br/licitacoes?codigo_municipio=' + codigoDoMunicipio + '&data_realizacao_autuacao_licitacao=2010-01-01_2023-12-31')
# except:
#     print("Tentando conexao com API TCE...")
#     try:
#         rContratos = requests.get(myurl)
#         # rLicitacao = requests.get('https://api-dados-abertos.tce.ce.gov.br/licitacoes?codigo_municipio=' + codigoDoMunicipio + '&data_realizacao_autuacao_licitacao=2010-01-01_2023-12-31')
#     except:
#         print("Não foi possivel conectar-se a API.")
#         os.system("PAUSE")
#         quit()
        
contratosNaoExistentes = []
licitacoesNaoExistentes = []

with open('C:/Users/Supor/Documents/python/Teste Arquivos SIM/arquivos/contratos.json') as arquivo:
    dados = json.load(arquivo)
listaDeContratos = dados['data']

with open('C:/Users/Supor/Documents/python/Teste Arquivos SIM/arquivos/licitacoes.json') as arquivo:
    dados = json.load(arquivo)
listaDeLicitacoes = dados['data']

for data in dataNE:
    if data[24].replace('"',"") == "":
        continue
    
    #Checando contrato
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
            print("Contrato " + data[24].replace('"',"") + " duplicado.")
            break
            
        elif contratoNoSIM and contratoNoArquivoCO == False:
            break
        
        elif contratoNoSIM == False and contratoNoArquivoCO == False:
            print("Contrato " + data[24].replace('"',"") + " invalido no arquivo CO.")
            break
            
        elif contratoNoSIM == False and contratoNoArquivoCO == True:
            print("Contrato " + data[24].replace('"',"") + " OK.")
            break
        
        
    #Checando Licitacao
    # licitacaoNaoExiste = True
    # while licitacaoNaoExiste:        
    #     for i, licitacao in enumerate(listaDeLicitacoes, start=1):
    #         if data[26].replace('"',"") == licitacao['numero_licitacao'] and data[27].replace('"',"") == licitacao['data_realizacao_autuacao_licitacao'].replace("-",""):
    #             licitacaoNaoExiste = False
                
    #     if licitacaoNaoExiste == False:
    #         break
        
    #     elif licitacaoNaoExiste == True:
    #         licitacoesNaoExistentes.append(data[24].replace('"',""))
    #         break
            
print("Contratos inexistentes" + str(contratosNaoExistentes))
print("Licitacoes inexistentes" + str(licitacoesNaoExistentes))
os.system("PAUSE")