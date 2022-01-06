#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:14:40 2021

@author: lyliana
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:00:31 2021

@author: lyliana
"""
#Nome: Lyliana Myllena Santos de Sousa
#NUSP:11223740
# Exercícios 1

import time

#Definirei a classe Pilha Lista, para construir a função classificação Quick

class PilhaLista:
    
    # Construtor da classe PilhaLista
    def __init__(self):
        self.pilha = []
    
    def __len__(self):
        return len(self.pilha)
    
    # retorna True se pilha vazia
    def vazia(self):
        return len(self.pilha) == 0
    
    # empilha novo elemento elem
    def push(self, elem):
            self.pilha.append(elem)           

    # retorna o elemento no tomo da lista
    def topo(self):
        if self.vazia():
            raise ValueError('Pilha vazia')

        return self.pilha[-1]

    # desempilha elemento, com uma exceção se pilha for vazia
    def pop(self):
        if self.vazia():
            raise ValueError('Pilha vazia')

        return self.pilha.pop()
 
    # imprime a pilha
    def __str__(self):
        
        return str(self.pilha)
    
#Criarei uma função para ler o arquivo e montar a list tab
def criandoTAB(nome):
    lines = []
    with open(nome) as f:
       lines = f.readlines()
    TAB = []
    for line in lines:
        TAB += [line.split(',')] 
        
    return TAB

#Criarei a função particiona para utilizar na classificação Quick
def particiona(TAB, inicio, fim, ordem):
    n = len(TAB)
    i, j = inicio, fim
    pivo = TAB[fim]
    primeiro = int(ordem[0]) - 1
    segundo = int(ordem[1]) - 1
    terceiro = int(ordem[2]) - 1
    
    for i in range(n):
            while i < j and TAB[i][primeiro] <= pivo[primeiro]:
                if TAB[i][primeiro] == pivo[primeiro]:
                    while i < j and TAB[i][segundo] <= pivo[segundo]:
                        if TAB[i][segundo] == pivo[segundo]:
                            while i < j and TAB[i][terceiro] <= pivo[terceiro]:
                                i = i + 1
                            if i < j:
                                TAB[i], TAB[j] = pivo, TAB[i]
                            else:
                                break
                            # diminuindo j
                            while i < j and TAB[j][terceiro]  >= pivo[terceiro]: 
                                j = j - 1
                            if i < j: 
                                TAB[i], TAB[j] = TAB[j], pivo
                            else: 
                                break
                        i = i + 1
                    if i < j:
                        TAB[i], TAB[j] = pivo, TAB[i]
                    else:
                        break
                    # diminuindo j
                    while i < j and TAB[j][segundo]  > pivo[segundo]: 
                        j = j - 1
                    if i < j: 
                        TAB[i], TAB[j] = TAB[j], pivo
                    else: 
                        break
                i = i + 1
            if i < j:
                TAB[i], TAB[j] = pivo, TAB[i]
            else:
                break
            # diminuindo j
            while i < j and TAB[j][primeiro]  > pivo[primeiro]: 
                j = j - 1
            if i < j: 
                TAB[i], TAB[j] = TAB[j], pivo
            else: 
                break
     
    return i

#Criarei a função crescente para usar no argumento da função sort
def crescente(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g

#Criarei agora três funções que classificaram a minha tabela TAB, onde ordem 
#será uma lista de com três caracteres numéricos

#função que classifica TAB pelo método da Bolha
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

    

#função que classifica TAB pelo método Quick não recursivo
def ClassificaQuick(TAB, ordem):
    t1 = time.time()
    # Cria a pilha de sub-listas e inicia com lista completa
    Pilha = PilhaLista()
    Pilha.push((0, len(TAB) - 1))
    # Repete até que a pilha de sub-listas esteja vazia
    
    #nesse primeiro for, inverterei a data em uma lista, para conseguir classificar pela ano
    for i in range(len(TAB)):
                s = TAB[i][2] 
                k = s.split('/') 
                TAB[i][2]= list(reversed(k))
    while not Pilha.vazia():
            inicio, fim = Pilha.pop()
            # Só particiona se há mais de 1 elemento
            if fim - inicio > 0:
                k = particiona(TAB, inicio, fim, ordem)
                # Empilhe as sub-listas resultantes
                Pilha.push((inicio, k - 1))
                Pilha.push((k + 1, fim))
    
    TABnovo = TAB[:]
    for i in range(len(TAB)):
                s = list(reversed(TAB[i][2]))
                k = '/'.join(s) 
                TABnovo[i][2]= k
   
    t2 = time.time()       
    print('Tempo de classificação Quick =', t2 - t1) 
    return TABnovo


#função que classifica TAB usando o método sort() do Python
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
    print('\n')             
    return TABnovo

#Por fim, criarei a função comparação, para comparar as tabelas
def Comparação(a,b):
    for i in range(len(a)):
        
        if a[i] != b[i]:
            print('*** Classificação incorreta\n')
            break
        
    print('*** Classificação correta\n')



if __name__ == '__main__':
    
    while True:
        nome = input("Nome do arquivo de origem:")
        if nome == "fim":
            break
        TAB = criandoTAB(nome)
        while True:
            TAB1 = TAB2 = TAB3 = TAB[:]
            o = input("Ordem da classificação:")
            if o == "fim":
                break
            ordem = list(o)
            ClassificaSort(TAB1, ordem)
            ClassificaBolha(TAB2, ordem)
            Comparação(TAB1,TAB2)
            ClassificaQuick(TAB3, ordem)
            Comparação(TAB1,TAB3)