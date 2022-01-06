#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 09:43:37 2021

@author: lyliana
"""
#Nome: Lyliana Myllena Santos de Sousa
#NUSP:11223740
# Exercícios 3

#Criarei uma função para ler o arquivo e montar a lista tab
def criandoTAB(arquivo):
    lines = []
    with open(arquivo) as f:
       lines = f.readlines()
    TAB = []
    for line in lines:
        TAB += [line.split(',')] 
        
    return TAB

#Separando as partes dos nomes da tabela TAB e um uma segunda tabela, onde cada nome
def criandoTABnome(TAB):
    TABnome = []
    prep = ['de', 'da', 'dos']
    for i in range(len(TAB)):
        a = [str(TAB[i][1]).lower().split()]
        #Não considere como nomes as preposições
        if prep[0] in a:
            a.remove(prep[0])
        
        TABnome += a
    return TABnome

#Essa é a nossa primeira função hash
def hash1(item, hash_table):
    M = len(hash_table)
    s = 0
    # s conterá a soma dos valores numéricos dos caracteres
    for chr in item:
        s = s + ord(chr)
    return s % M # valor da função

#Essa é a nossa segunda função hash com um passo de 3
def hash2(item, hash_table):
    M = len(hash_table)
    s = 0
    # s conterá a soma dos valores numéricos dos caracteres
    for chr in item:
        s = s + ord(chr)
    return (3 + s) % M # valor da função

#Criando a função que estrutura a tabela hash
def estruturahash(TABnome):
    #Irei supor que uma pessoa possui 10 "palavras" em seu nome, portanto o tamanho da nossa tabela
    #hash será 10*(comprimento da tabela nome). Ou seja supondo que todas as pessoas possuem no máximo 10
    #nomes e que todos os nomes são diferentes, teremos espaço suficiente para comportar todos os elementos
    hash_table = [None] * (10*len(TABnome))
    return hash_table
    
#Essa função adiciona as informações na TAB_HASH, tabela solicitada no enunciado
def double_hashing(hash_table, item, position):
    M = len(hash_table)
    h1 = hash1(item, hash_table)
    h2 = hash2(item, hash_table)
    for i in range(len(hash_table)):
        if hash_table[(h1 + i * h2) % M] is None:
            hash_table[(h1 + i * h2) % M] = [item,position]
            break
        if hash_table[(h1 + i * h2) % M][0] == item:
            hash_table[(h1 + i * h2) % M] == hash_table[(h1 + i * h2) % M].append(position)

#Essa função utiliza o espaço criado pela lista hash_table, para criar a nossa lista TAB_HASH, pedida no enunciado
def TAB_HASH(TABnome,hash_table):
    for i in range(len(TABnome)):
        for j in range(len(TABnome[i])):
            item = TABnome[i][j]
            position = i
            double_hashing(hash_table, item, position)
    return hash_table

#Crio a função que busca por um item na tabela hash
def search(hash_table, item):
    M = len(hash_table)
    h1 = hash1(item, hash_table)
    h2 = hash2(item, hash_table)
    for i in range(len(hash_table)):
        if hash_table[(h1 + i * h2) % M][0] == item:
            return (h1 + i * h2) % M
    
    
     
#printa as linhas que possuem o valor informado
def printa(indice_TAB_HASH, TAB_HASH , TAB):
    listaprint = TAB_HASH[int(indice_TAB_HASH)]
    i = 1
    while i < len(listaprint):
        print(TAB[listaprint[i]][0],',',TAB[listaprint[i]][1],',',TAB[listaprint[i]][2])
        i += 1
    print('* * * ', len(listaprint) - 1,' comparações para localizar os nomes' )
    
if __name__ == '__main__':
    
        arquivo = input("Entre com o nome do arquivo:")
        TAB = criandoTAB(arquivo)
        TABnome = criandoTABnome(TAB)
        hash_table = estruturahash(TABnome)
        TAB_HASH = TAB_HASH(TABnome,hash_table)
        while True:
            valor = str(input("Entre com um valor:"))
            if valor == "fim": 
                break
            indice_TAB_HASH = search(hash_table, valor.lower())
            printa(indice_TAB_HASH, TAB_HASH , TAB)