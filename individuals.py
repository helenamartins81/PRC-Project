import csv
import re
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

with open('contestants.csv',"r", newline='') as musicas:
    data = list(csv.reader(musicas))[1:]

#apenas para ver as votações


df = pd.read_excel('eurovision_song_contest_1975_2021.xlsx', sheet_name=None)

d = { " ": "_", "'": "_", "&":"", ",":"_", "(":"", ")":"", ".":""}

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


#artistas
for ind in data:
    print('###  http://www.di.uminho.pt/prc2021/eurovision#' + replace_all(ind[3],d))
    print(f":{replace_all(ind[3],d)} rdf:type owl:NamedIndividual ,")
    print(f"\t\t\t:Artista ;")
    print(f"\t\t:interpretaMúsica :m{ind[0]}{ind[1]} ;")
    print(f"\t\t:representaPaís :{ind[1]} ;")
    print(f"\t\t:nome '{replace_all(ind[3],d)}' .")

#compositores -> faltam os de 2020 no dataset
for i in data:
    if i[17]:
        x = i[17].split(";")
        l = 0
        for k in x:
            print('###  http://www.di.uminho.pt/prc2021/eurovision#' + replace_all(k,d))
            print(f":{replace_all(k,d)+str(l)} rdf:type owl:NamedIndividual ,")
            print(f"\t\t\t:Compositor ;")
            print(f"\t\t:compõe :m{i[0]}{i[1]} ;")
            print(f"\t\t:nome '{replace_all(k,d)}' .")
            l+=1


#Liricistas -> faltam os de 2020 no dataset
for i in data:
    if i[18]:
        x = i[18].split(";")
        l = 0
        for k in x:
            print('###  http://www.di.uminho.pt/prc2021/eurovision#' + replace_all(k,d))
            print(f":{replace_all(k,d)+str(l)} rdf:type owl:NamedIndividual ,")
            print(f"\t\t\t:Liricista ;")
            print(f"\t\t:escreve :m{i[0]}{i[1]} ;")
            print(f"\t\t:nome '{replace_all(k,d)}' .")
            l+=1


#completar a parte dos eventos com o outro dataset
#edição
lista = []
for i in data:
    lista.append(i[0])
    lista = list(dict.fromkeys(lista))
  
for k in lista:
    print('###  http://www.di.uminho.pt/prc2021/eurovision#ed' + k)
    print(f":ed{k} rdf:type owl:NamedIndividual ,")
    print(f"\t\t\t:Edição ;")
    print(f"\t\t:organizadaPor : ;")
    print(f"\t\t:temEvento :final{k} ;")
    print(f"\t\t:anoEdição {k} .")



#completar com a parte de recber pontos
#classificação
for i in data:
    print('###  http://www.di.uminho.pt/prc2021/eurovision#c'+i[0]+i[1])
    print(f":c{i[0]+i[1]} rdf:type owl:NamedIndividual ,")
    print(f"\t\t\t:Classificação ;")
   # for j in df.index:
   #     if df["Year"][j] == i[0] and df["To country"][j] ==i[1] :
   #         print(f"\t\t:recebePontosDe " + df["From country"][j] +" ;")
    print(f"\t\t:referenteA :final{i[0]} ;")
    print(f"\t\t:classificação {i[5]} ;")
    print(f"\t\t:juri {i[14]} ;")
    print(f"\t\t:televoto {i[13]} ;")
    print(f"\t\t:totalPontos {i[10]} .")
    

#falta a parte dos eventos em que participa e as musicas
#país
for ind in data:

    print('###  http://www.di.uminho.pt/prc2021/eurovision#' + ind[1].replace(' ','_'))
    print(f":{ind[1].replace(' ','_')} rdf:type owl:NamedIndividual ,")
    print(f"\t\t\t:País ;")
    print(f"\t\t:participaEm  ;")
    print(f"\t\t:temMúsica ;")
    print(f"\t\t:nome '{replace_all(ind[2],d)}' .")



#só tem as finais
#evento
for j in lista:
    print('###  http://www.di.uminho.pt/prc2021/eurovision#final' + j)
    print(f":final{j} rdf:type owl:NamedIndividual ,")
    print(f"\t\t\t:Evento ;")
    print(f"\t\t:tipoEvento final .")


#música
for ind in data:
    print('###  http://www.di.uminho.pt/prc2021/eurovision#m' + ind[0]+ind[1])
    print(f":m{ind[0]+ind[1]} rdf:type owl:NamedIndividual ,")
    print(f"\t\t\t:Música ;")
    print(f"\t\t:duração  ;")
    print(f"\t\t:letra  ;")
    print(f"\t\t:título '{replace_all(ind[4],d)}' .")



