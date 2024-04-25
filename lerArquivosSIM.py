from pathlib import Path
import os

municipio = ''

nes = 'NE2'
listaDeNEsNaPasta = []
dataNE = []

lis = 'LI2'
listaDeLIsNaPasta = []
dataLI = []

cos = 'CO2'
listaDeCOsNaPasta = []
dataCO = []

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "arquivos/"
caminho = os.path.join(script_dir, rel_path)
pathLote = Path(caminho)

#Arquivo NE
if pathLote.exists():
    for f in os.listdir(pathLote):
        if nes in f:
            listaDeNEsNaPasta.append(f)
        
for ne in listaDeNEsNaPasta:
    with open(caminho + ne, "r") as arquivoNE:
        linhasDoArquivo = arquivoNE.readline()
        while linhasDoArquivo:
            dataNE.append(linhasDoArquivo.split(","))
            linhasDoArquivo = arquivoNE.readline()
#Arquivo CO
if pathLote.exists():
    for h in os.listdir(pathLote):
        if cos in h:
            listaDeCOsNaPasta.append(h)
        
for co in listaDeCOsNaPasta:
    with open(caminho + co, "r") as arquivoCO:
        linhasDoArquivo = arquivoCO.readline()
        while linhasDoArquivo:
            dataCO.append(linhasDoArquivo.split(","))
            linhasDoArquivo = arquivoCO.readline()
            
#Arquivo LI
if pathLote.exists():
    for g in os.listdir(pathLote):
        if lis in g:
            listaDeLIsNaPasta.append(g)
        
for li in listaDeLIsNaPasta:
    with open(caminho + li, "r") as arquivoLI:
        linhasDoArquivo = arquivoLI.readline()
        while linhasDoArquivo:
            dataLI.append(linhasDoArquivo.split(","))
            linhasDoArquivo = arquivoLI.readline()
            
municipio = dataNE[0][1].replace('"',"")