#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 17:30:43 2021

@author: lyliana
"""

#Nome: Lyliana Myllena Santos de Sousa
#NUSP:11223740
# Exercícios 4 – Busca de palavras em texto

"""Nesta atividade criaremos um buscador por palavras, que busca uma determinada sequencia de caracteres 
e conta quantas vezes localizou essa sequencia ao longo do texto"""
import time

#Criarei uma função para ler o arquivo
def lendo(nome):
    texto =  open(nome, "r",  encoding="latin-1").read()
     
    return texto

#Função que usará a função Intrínseca da python Count
def pycount(palavra, texto):
    t1 = time.time()
    contador = texto.count(palavra)
    t2 = time.time()
    t = t2 - t1
    print(f'count:  Encontrada {contador} vezes em {t} segundos')
    
#Função que usará o método elementar de busca (deslocamento de 1 em 1)
def bpNORMAL(palavra, texto):
    t1 = time.time()
    a = palavra
    b = texto
    m, n = len(a), len(b)
    contador = 0
    for k in range(n - m + 1):
        i, j = 0, k
        while i < m:
            if a[i] != b[j]: 
                break
            i, j = i + 1, j + 1
        if i == m: 
            contador += 1
    t2 = time.time()
    t = t2 - t1
    print(f'Normal: Encontrada {contador} vezes em {t} segundos')
    
#Função que usará o método Boyer-Moore 1 (deslocamento baseado no próximo caractere do texto)
def bpBM1(palavra, texto):
    t1 = time.time()
    a = palavra
    b = texto
    m, n = len(a), len(b)
    contador = 0
    ult = [-1] * 256
    for k in range(m):
        ult[ord(a[k])] = k
    k = m - 1
    while k < n:
        j, i = k, m - 1
        while i >= 0:
            if a[i] != b[j]:
                break
            j, i = j - 1, i - 1
        if i < 0:
            contador += 1
        
        if k + 1 >= n: 
            break
        
        k = k + m - ult[ord(b[k+1])]
     
    t2 = time.time()
    t = t2 - t1
    print(f'BM1:    Encontrada {contador} vezes em {t} segundos')

if __name__ == '__main__':
     
        nome = input("Entre com o nome do arquivo de texto:")
        texto = lendo(nome)
        
        while True:
            palavra = input("Entre com a palavra a procurar:")
            if palavra == "#":
                break
            pycount(palavra, texto)
            bpNORMAL(palavra, texto)
            bpBM1(palavra, texto)