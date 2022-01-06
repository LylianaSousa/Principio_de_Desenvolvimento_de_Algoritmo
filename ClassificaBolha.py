#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 18:13:03 2021

@author: lyliana
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:45:14 2021

@author: lyliana
"""
import time 

#Teste pra classificar pela método da bolha
def criandoTAB(nome):
    lines = []
    with open(nome) as f:
       lines = f.readlines()
    TAB = []

    for line in lines:
        TAB += [line.split(',')] 
        
    return TAB

#criando a funãço classificação
def ClassificaBolha(TAB, ordem):
    t1 = time.time()
    n = len(TAB)
    primeiro = int(ordem[0]) - 1
    segundo = int(ordem[1]) - 1
    terceiro = int(ordem[2]) - 1
    
    #nesse primeiro for, inverterei a data em uma lista, para conseguir classificar pela ano
    for i in range(n):
                s =TAB[i][2] 
                TAB[i][2] =  s.split('/')
   
    #quando chegar no elemento 3 da ordem, ele entrara no if e classificará pelo ano
    
    #Primeira classificação
    if primeiro == 2:
            
            for i in range(1,n):
                j = i
                   
                while j > 0 and TAB[j][primeiro][2]< TAB[j-1][primeiro][2]:
                            
                            TAB[j], TAB[j - 1] = TAB[j - 1], TAB[j]
                            j = j - 1
    else:
        for i in range(1,n):
            j = i
             
            while j > 0 and TAB[j][primeiro]< TAB[j-1][primeiro]:
                            
                            TAB[j], TAB[j - 1] = TAB[j - 1], TAB[j]
                            j = j - 1
    
     
    #Segunda classificação
    if segundo == 2:
            
            for i in range(1,n):
                j = i
                if TAB[j][primeiro] == TAB[j-1][primeiro]:   
                    while j > 0 and TAB[j][segundo][2]< TAB[j-1][segundo][2]:
                                
                                TAB[j], TAB[j - 1] = TAB[j - 1], TAB[j]
                                j = j - 1
    else:
        for i in range(1,n):
            j = i
            
            if TAB[j][primeiro] == TAB[j-1][primeiro]:
                while j > 0 and TAB[j][segundo]< TAB[j-1][segundo]:
                      TAB[j], TAB[j - 1] = TAB[j - 1], TAB[j]
                      j = j - 1
                      
    #Terceira classificação
    if terceiro == 2:
            
            for i in range(1,n):
                j = i
                if TAB[j][primeiro] == TAB[j-1][primeiro]:  
                    if TAB[j][segundo] == TAB[j-1][segundo]:
                        while j > 0 and TAB[j][terceiro][2]< TAB[j-1][terceiro][2]:
                                    
                                    TAB[j], TAB[j - 1] = TAB[j - 1], TAB[j]
                                    j = j - 1
    else:
        for i in range(1,n):
            j = i
            
            if TAB[j][primeiro] == TAB[j-1][primeiro]:
                if TAB[j][segundo] == TAB[j-1][segundo]:
                    while j > 0 and TAB[j][terceiro]< TAB[j-1][terceiro]:
                          TAB[j], TAB[j - 1] = TAB[j - 1], TAB[j]
                          j = j - 1
    
    #Voltarei a tabela para o formato original                   
    TABnovo = TAB[:]
    for i in range(n):
                s =TAB[i][2] 
                TABnovo[i][2] = '/'. join(s)
   
    t2 = time.time()
    print('Tempo de classificação Bolha =', t2 - t1)                
    return TABnovo

if __name__ == '__main__':
 
        nome = 'testes1.txt'
        TAB = criandoTAB(nome)
        TAB1 = TAB2 = TAB
        ordem = list('213')
        print(ClassificaBolha(TAB, ordem))