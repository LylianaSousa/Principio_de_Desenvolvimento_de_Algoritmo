#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 08:48:12 2021

@author: lyliana
"""
#Nome: Lyliana Myllena Santos de Sousa
#NUSP:11223740
# Exercícios 1


""""Neste exercício foi fornecido duas funções, Haroi e Movimente,
e o nosso trabalho será imprimir os resultados de acordo com o enunciado.
Para isso criarei três outras funções e acrescentarei alguns parametro
nas funções dadas."""

""" Na função Hanoi eu acrescentei um paraamêtro chamado de t que nos dá a estrutura
das torres com um número de discos n. Dentro da função movimente, eu támbém 
acrescentei mais dois parametros, sendo eles a estrutura da torre e o numero de
discos nela """       
 
def Hanoi(n,t, torreA, torreB, torreAux):
     
    if n == 1:
        # mover disco 1 da torreA para a torreB
        Movimente(n,t,1, torreA, torreB)
    else:
        # n - 1 discos da torreA para torreAux com torreB auxiliar
        Hanoi(n - 1, t, torreA, torreAux, torreB)
        # mover disco n da torreA para torreB
        Movimente(n,t,n,  torreA,torreB)
        # n - 1 discos da torreAux para a torreB com torreA auxiliar
        Hanoi(n - 1, t, torreAux, torreB, torreA)

""" Além de acrescentar os novos paramêtros na função Movimente, eu acrescentei
mais duas linhas, onde a primeira chama a função movimentadiscos, que reestrututra
as torres de acordo com os parametros informados pela função Movimente, na segunda 
linha eu imprimo a nova organização dos discos"""

def Movimente(n,t,k, origem, destino):
    print("mover disco ", k, " da torre ", origem, " para a torre ", destino) 
    m = movimentadiscos(k, origem, destino,t)
    print(imprimitorre(n,m))

""" A função torres cria uma matriz torre com a estrutura inicial do jogo,
 de acordo com o número de discos n """

def torres(n):
    torre0 = [i for i in range(n, 0, -1)]
    torre1 = []
    torre2 = []
    
    torre = [torre0, torre1, torre2]
    
    return torre 

""" A função imprimitorre pega a matriz que a função torres fornece e imprimi ela 
de acordo com o padrão pedido no enunciado"""

def imprimitorre(n,torre):
        entrada = ""
        for i in range(n, -1, -1):
            for j in range(3):
                if len(torre[j]) > i:
                    entrada += " " + str(torre[j][i])
                else:
                    entrada += "  "
            entrada += "\n"

        return entrada + " A B C"
    
""" A função movimentadiscos utiliza alguns dos parametros dados pela função 
Movimente para alterar a estrututra da matriz, removendo o disco do topo da 
pilha origem e adicionando o no topo da pilha destino"""    

def movimentadiscos(k, origem, destino,t):
    
    t0 = t[0]
    t1 = t[1]
    t2 = t[2]
          
    if origem == 0:
        t0.pop()
             
        if destino == 1:
            t1.append(k)
        else: 
            
            t2.append(k)
            
    elif origem == 1:
        t1.pop()
           
        if destino == 0:
            
            t0.append(k)
        else:
            
            t2.append(k)
            
    elif origem == 2:
        t2.pop()
            
        if destino == 1:
            
            t1.append(k)
        else:
            
            t0.append(k)
    return t 
       

#Para ultizar a função Hanoi, primeiro preciso definir o número de disco
n = 2   
print(f"\n* * * Movimentar {n} discos * * *")
Hanoi( n, torres(n) , 0, 1, 2)