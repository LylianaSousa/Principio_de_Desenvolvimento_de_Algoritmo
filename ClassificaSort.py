#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:45:48 2021

@author: lyliana
"""
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

#essa será a nossa função que organizará em ordem crescente nossa tabela
def crescente(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g

#essa é a minha função classificação
def ClassificaSort(TAB, ordem):
    t1 = time.time()
    primeiro = int(ordem[0]) - 1
    segundo = int(ordem[1]) - 1
    terceiro = int(ordem[2]) - 1
    
    #nesse primeiro for, inverterei a data em uma lista, para conseguir classificar pela ano
    for i in range(len(TAB)):
                s = TAB[i][2] 
                k = s.split('/') 
                TAB[i][2]= list(reversed(k))
                
    TAB.sort(key = crescente(primeiro, segundo, terceiro))  
    
    #Voltarei a tabela para o formato original
    TABnovo = TAB[:]
    for i in range(len(TAB)):
                s = list(reversed(TAB[i][2]))
                k = '/'.join(s) 
                TABnovo[i][2]= k
    t2 = time.time()
    print('Tempo de classificação Sort =', t2 - t1)                
    return TABnovo

if __name__ == '__main__':
 
        nome = 'testes1.txt'
        TAB = criandoTAB(nome)
        TAB1 = TAB2 = TAB
        ordem = list('321')
        print(ClassificaSort(TAB, ordem))