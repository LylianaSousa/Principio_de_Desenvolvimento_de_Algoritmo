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
#e o nosso trabalho será imprimir os resultados de acordo com o enunciado
#Para isso criarei uma terceira função imprimi """

        
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

def Movimente(n,t,k, origem, destino):
    print("mover disco ", k, " da torre ", origem, " para a torre ", destino) 
    m = movimentadiscos(k, origem, destino,t)
    print(imprimitorre(n,m))

def torres(n):
    torre0 = [i for i in range(n, 0, -1)]
    torre1 = []
    torre2 = []
    
    torre = [torre0, torre1, torre2]
    
    return torre 

def imprimitorre(n,torre):
        output = ""
        for i in range(n, -1, -1):
            for j in range(3):
                if len(torre[j]) > i:
                    output += " " + str(torre[j][i])
                else:
                    output += "  "
            output += "\n"

        return output + " A B C"
    
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
       

   
print("\n* * * Movimentar 2 discos * * *")
Hanoi( 2, torres(2) , 0, 1, 2)
