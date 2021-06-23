import csv
import re
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

with open('contestants.csv',"r", newline='') as musicas:
    data = list(csv.reader(musicas))[1:]


with open('eurovision_song_contest_1975_2021.csv',"r", newline='') as musicas:
    data2 = list(csv.reader(musicas))[1:]
#apenas para ver as votações


df = pd.read_excel('eurovision_song_contest_1975_2021.xlsx', sheet_name=None)

d = { " ": "_", "'": "_", "&":"", ",":"_", "(":"", ")":"", ".":""}

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


#artistas
for ind in data:
  
    print('###  http://www.di.uminho.pt/prc2021/eurovision#' + replace_all(ind[4],d))
    print(f":{replace_all(ind[4],d)} rdf:type owl:NamedIndividual ,")
    print(f"\t\t\t:Artista ;")
    print(f"\t\t:interpretaMúsica :m{ind[0]}_{replace_all(ind[2],d)} ;")
    print(f"\t\t:representaPaís :{replace_all(ind[2],d)} ;")
    print(f"\t\t:nome '{replace_all(ind[4],d)}' .")

#compositores -> faltam os de 2020 no dataset
for i in data:
    if i[18]:
        x = i[18].split(";")
        l = 0
        for k in x:
            print('###  http://www.di.uminho.pt/prc2021/eurovision#' + replace_all(k,d))
            print(f":{replace_all(k,d)+str(l)} rdf:type owl:NamedIndividual ,")
            print(f"\t\t\t:Compositor ;")
            print(f"\t\t:compõe :m{i[0]}_{i[2]} ;")
            print(f"\t\t:nome '{replace_all(k,d)}' .")
            l+=1


#Liricistas -> faltam os de 2020 no dataset
for i in data:
    if i[19]:
        x = i[19].split(";")
        l = 0
        for k in x:
            print('###  http://www.di.uminho.pt/prc2021/eurovision#' + replace_all(k,d))
            print(f":{replace_all(k,d)+str(l)} rdf:type owl:NamedIndividual ,")
            print(f"\t\t\t:Liricista ;")
            print(f"\t\t:escreve :m{i[0]}_{i[2]} ;")
            print(f"\t\t:nome '{replace_all(k,d)}' .")
            l+=1



#completar a parte dos eventos com o outro dataset
#edição
for i in data:
    print('###  http://www.di.uminho.pt/prc2021/eurovision#ed' + i[0])
    print(f":ed{i[0]} rdf:type owl:NamedIndividual ,")
    print(f"\t\t\t:Edição ;")
    print(f"\t\t:organizadaPor : '{i[1]}' ;")
    print(f"\t\t:anoEdição {i[0]} .")


lista = []
for i in data:
    lista.append(i[0])
    lista = list(dict.fromkeys(lista))



#completar com a parte de recber pontos
#classificação
for i in data:
    print('###  http://www.di.uminho.pt/prc2021/eurovision#c'+i[0]+i[2])
    print(f":c{i[0]+i[2]} rdf:type owl:NamedIndividual ,")
    print(f"\t\t\t:Classificação ;")
    print(f"\t\t:referenteA :final{i[0]} ;")
    if i[6]== '':
        print(f"\t\t:classificação 0 ;")   
    else:
        print(f"\t\t:classificação {i[6]} ;")
    if i[15]== '':
        print(f"\t\t:juri 0 ;")  
    else:
        print(f"\t\t:juri {i[15]} ;")
    if i[14]== '':
        print(f"\t\t:televoto 0 ;")
    else:
        print(f"\t\t:televoto {i[14]} ;")
    if i[11]=='':
        print(f"\t\t:totalPontos 0 .")
    else:
        print(f"\t\t:totalPontos {i[11]} .")

#falta a parte dos eventos em que participa e as musicas
#país
for ind in data:

    print('###  http://www.di.uminho.pt/prc2021/eurovision#' + ind[3].replace(' ','_'))
    print(f":{ind[3].replace(' ','_')} rdf:type owl:NamedIndividual ,")
    print(f"\t\t\t:País ;")
    print(f"\t\t:participaEm  ;")
    print(f"\t\t:temMúsica ;")
    print(f"\t\t:nome '{replace_all(ind[3],d)}' .")

#música
for ind in data:
    print('###  http://www.di.uminho.pt/prc2021/eurovision#m' + ind[0]_ind[2])
    print(f":m{ind[0]+ind[2]} rdf:type owl:NamedIndividual ,")
    print(f"\t\t\t:Música ;")
    print(f"\t\t:link '{ind[21]}' ;")
    print(f"\t\t:título '{replace_all(ind[5],d)}' .")

