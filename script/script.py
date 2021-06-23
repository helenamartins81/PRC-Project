import csv
import re
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

with open('contestants.csv',"r", newline='') as musicas:
    data = list(csv.reader(musicas))[2:]

d = { " ": "_", "'": "_", "&":"", ",":"_", "(":"", ")":"", ".":"", "\"" : "" }

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


#liricista
for ind in data:
    #liricista
    if ind[19]!='':
        lista=ind[19].split(";")
        for i in lista:
            print(f'###  http://www.di.uminho.pt/prc2021/eurovision#L_{replace_all(i,d)}')
            print(f'<http://www.di.uminho.pt/prc2021/eurovision#{replace_all(i,d)}> rdf:type owl:NamedIndividual ,')
            print(f'                <http://www.di.uminho.pt/prc2021/eurovision#Liricista> ,')
            print(f'        <http://www.di.uminho.pt/prc2021/eurovision#Pessoa> ;')
            print(f'        <http://www.di.uminho.pt/prc2021/eurovision#escreve> <http://www.di.uminho.pt/prc2021/eurovision#m{ind[0]}_{replace_all(ind[3],d)}> ;')
            print(f'        <http://www.di.uminho.pt/prc2021/eurovision#nome> "{replace_all(i,d)}" .\n\n')

    #compositor
    if ind[18]!='':
        lista1=ind[18].split(";")
        for i in lista1:
            print(f'###  http://www.di.uminho.pt/prc2021/eurovision#C_{replace_all(i,d)}')
            print(f'<http://www.di.uminho.pt/prc2021/eurovision#{replace_all(i,d)}> rdf:type owl:NamedIndividual ,')
            print(f'            <http://www.di.uminho.pt/prc2021/eurovision#Compositor> ,')
            print(f'        <http://www.di.uminho.pt/prc2021/eurovision#Pessoa> ;')      
            print(f'        <http://www.di.uminho.pt/prc2021/eurovision#compõe> <http://www.di.uminho.pt/prc2021/eurovision#m{ind[0]}_{replace_all(ind[3],d)}> ;')
            print(f'        <http://www.di.uminho.pt/prc2021/eurovision#nome> "{replace_all(i,d)}" .\n\n')

    #pais
    print(f'###  http://www.di.uminho.pt/prc2021/eurovision#{replace_all(ind[3],d)}')
    print(f'<http://www.di.uminho.pt/prc2021/eurovision#{replace_all(ind[3],d)}> rdf:type owl:NamedIndividual ,')
    print(f'            <http://www.di.uminho.pt/prc2021/eurovision#País> ;')
    print(f'        <http://www.di.uminho.pt/prc2021/eurovision#temClassificação> <http://www.di.uminho.pt/prc2021/eurovision#class_{replace_all(ind[3],d)}_{ind[0]}> ;')
    print(f'        <http://www.di.uminho.pt/prc2021/eurovision#temMúsica> <http://www.di.uminho.pt/prc2021/eurovision#m{ind[0]}_{replace_all(ind[3],d)}> ;')
    print(f'        <http://www.di.uminho.pt/prc2021/eurovision#éRepresentadoPor> <http://www.di.uminho.pt/prc2021/eurovision#{replace_all(ind[4],d)}> ;')
    print(f'        <http://www.di.uminho.pt/prc2021/eurovision#nome> "{replace_all(ind[3],d)}" .\n\n')
    
    #artista
    if ind[4]!='':
        print(f'###  http://www.di.uminho.pt/prc2021/eurovision#{replace_all(ind[4],d)}')
        print(f'<http://www.di.uminho.pt/prc2021/eurovision#{replace_all(ind[4],d)}> rdf:type owl:NamedIndividual ,')
        print(f'            <http://www.di.uminho.pt/prc2021/eurovision#Artista> ,')
        print(f'        <http://www.di.uminho.pt/prc2021/eurovision#Pessoa> ;')
        print(f'        <http://www.di.uminho.pt/prc2021/eurovision#interpretaMúsica> <http://www.di.uminho.pt/prc2021/eurovision#m{ind[0]}_{replace_all(ind[3],d)}> ;')
        print(f'        <http://www.di.uminho.pt/prc2021/eurovision#representaPaís> <http://www.di.uminho.pt/prc2021/eurovision#{replace_all(ind[3],d)}> ;')
        print(f'        <http://www.di.uminho.pt/prc2021/eurovision#nome> "{replace_all(ind[4],d)}" .\n\n')

    #classificação
    if ind[6]!='':
        print(f'###  http://www.di.uminho.pt/prc2021/eurovision#class_{replace_all(ind[3],d)}_{ind[0]}')
        print(f'<http://www.di.uminho.pt/prc2021/eurovision#class_{replace_all(ind[3],d)}_{ind[0]}> rdf:type owl:NamedIndividual ,')
        print(f'            <http://www.di.uminho.pt/prc2021/eurovision#Classificação> ;')
        print(f'        <http://www.di.uminho.pt/prc2021/eurovision#foiClassificadoCom> <http://www.di.uminho.pt/prc2021/eurovision#{replace_all(ind[3],d)}> ;')
        print(f'        <http://www.di.uminho.pt/prc2021/eurovision#anoEdição> {ind[0]} ;\n\n')
        if ind[15]!='':
            print(f'        <http://www.di.uminho.pt/prc2021/eurovision#juri> {ind[15]} ;')
        
        if ind[14]!='':
            print(f'        <http://www.di.uminho.pt/prc2021/eurovision#televoto> {ind[14]} ;')
        
        if ind[11]!='':
            print(f'        <http://www.di.uminho.pt/prc2021/eurovision#totalPontos> {ind[11]} ;')
        print(f'        <http://www.di.uminho.pt/prc2021/eurovision#lugar> {ind[6]} .\n\n')

    #ediçao
    print(f'###  http://www.di.uminho.pt/prc2021/eurovision#ed{ind[0]}')
    print(f'<http://www.di.uminho.pt/prc2021/eurovision#ed{ind[0]}> rdf:type owl:NamedIndividual ,')
    print(f'            <http://www.di.uminho.pt/prc2021/eurovision#Edição> ;')
    if ind[6]=='1':
        print(f'        <http://www.di.uminho.pt/prc2021/eurovision#temPaísVencedor> <http://www.di.uminho.pt/prc2021/eurovision#{replace_all(ind[3],d)}> ;')
    print(f'        <http://www.di.uminho.pt/prc2021/eurovision#organizadaPor> <http://www.di.uminho.pt/prc2021/eurovision#{replace_all(ind[1],d)}> ;')
    print(f'        <http://www.di.uminho.pt/prc2021/eurovision#anoEdição> {ind[0]} .\n\n')

    #musica
    print(f'###  http://www.di.uminho.pt/prc2021/eurovision#m{ind[0]}_{replace_all(ind[3],d)}')
    print(f'<http://www.di.uminho.pt/prc2021/eurovision#m{ind[0]}_{replace_all(ind[3],d)}> rdf:type owl:NamedIndividual ,')
    print(f'            <http://www.di.uminho.pt/prc2021/eurovision#Música> ;')
    print(f'        <http://www.di.uminho.pt/prc2021/eurovision#link> "{ind[21]}" ;')
    print(f'        <http://www.di.uminho.pt/prc2021/eurovision#título> "{ind[5]}";\n\n')
    print(f'        <http://www.di.uminho.pt/prc2021/eurovision#anoEdição> {ind[0]} .\n\n')

    