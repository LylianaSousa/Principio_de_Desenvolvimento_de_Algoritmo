#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:09:18 2021

@author: lyliana
"""
#Nome: Lyliana Myllena Santos de Sousa
#NUSP:11223740
# Exercícios 3

class ListaDuplamenteLigada:
    
    #Vou criar uma class com duas funções, uma para definir os nós da lista duplamente ligada
    # e a outra para imprimir o valor desses nós
    
    class Node:
        
        __slots__ = 'valor', 'anterior', 'proximo'
         
        def __init__(self, valor, ante, prox):
            self.valor = valor
            self.anterior = ante
            self.proximo = prox
        
        def __str__(self):
                    
            return str(self.valor)
    
    #A seguir definirei a nossa lista duplamente ligada circular, junto com um conjunto de funções
    #para facilitar a manipulação da lista
    def __init__(self):
        self.primeiro = self.Node(None, None, None)
        self.ultimo = self.Node(None, None, None)
        self.primeiro.proximo = self.ultimo
        self.ultimo.anterior = self.primeiro
        self.tamanho = 0
    
    #retorna o tamanho da lista duplamente ligada
    def __len__(self):
        
        return self.tamanho
    
    #retorna True se a lista duplamente ligada estiver vazia
    def is_empty(self):
         
        return self.tamanho == 0
    
    #Busca um elemento da lista e nos retorna informações dos elementos anterior e próximo
    #que aparece ao lado dele primiero elemento val encontrado
    def Busca(self,val):
        percorre = self.primeiro
        while percorre:
            if percorre.valor == val:
                return [str(percorre.anterior), str(percorre.proximo)]
            else:
                percorre = percorre.proximo
        return ['None', 'None']
    
    # Adiciona um elemento ao final da lista
    def Adiciona(self, valor):
        comparacao = self.Busca(valor)
        if self.primeiro:
                
                aux = self.primeiro
                ant = None
                while aux.proximo:
                    ant = aux
                    aux = aux.proximo
                    if str(aux) <= str(comparacao[1]):
                        print("to aqui")
                        
                        
                aux.proximo = self.Node(valor,ant, None)
                aux.proximo.anterior = aux
                aux.anterior = ant
                if self.ultimo:
                    self.ultimo = aux.proximo
        else:
                self.primeiro = self.Node(valor,ant, None)
                self.ultimo = self.Node(valor,ant, None)
       
        self.tamanho += 1
        
    #conta quantas vezes um elemento x aparece na lista duplamente ligada
    def Conta(self, x):
        i = 0
        percorre = self.primeiro
        while percorre:
            if str(percorre.valor) == str(x):
                i +=1
            percorre = percorre.proximo
        return i
    
    #remove todos os elementos x da lista duplamente ligada
    def Remove(self,x):
        n = self.Conta(x)
        i = 0
        for i in range(n):
            if self.is_empty():
                return None
            percorre = self.primeiro.proximo
            while percorre != None and percorre.valor != x:
                percorre = percorre.proximo
            if percorre ==  None:
                return None
            elif percorre.proximo == None:
                x = percorre.valor
                percorre.anterior.proximo = None
                self.ultimo = percorre.anterior
                i += 1
                del percorre
            else:
                x = percorre.valor
                percorre.proximo.anterior = percorre.anterior
                percorre.anterior.proximo = percorre.proximo
                del percorre
                
        return n

    #imprimi a lista duplamennte ligada de acordo com o que foi pedido no enunciado
    def __str__(self):
        # Mostra os elementos da lista duplamente ligada, mostrando também o anterior e o sucessor.
        valor = 'Nó ' + ' Anterior ' + ' Informação ' + ' Posterior \n'
        n = 2 + self.tamanho
        no = list(range(1,n+1,1))
        i = 0
        if self.primeiro is not None:
            percorre = self.primeiro
           
            while percorre.proximo:
              
                percorre = percorre.proximo
                valor += '\n'
                valor += " " + str(no[i]) + "   " + str(percorre.anterior) + "       " + str(percorre.valor) + "        " + str(percorre.proximo)
                i += 1
                
           
            valor += '\n' +" " + str(no[i]) + "   " + str(percorre.valor) + "      " + str(percorre.proximo) + "        " + str(None)
                
            
        return valor
        
if __name__ == "__main__":      
    lista = ListaDuplamenteLigada()
    print(lista)
    print("--------------------------------")
    lista.Adiciona("Antonio")
    print(lista)
    print("--------------------------------")
    lista.Adiciona("Maria")
    print(lista)
    print("--------------------------------")
    lista.Adiciona("Ana")
    print(lista)
    print("--------------------------------")
    lista.Adiciona("Antonio")
    print(lista)
    print("--------------------------------")
    print('quantas vezes aparece: Antonio ->',lista.Conta('Antonio'))
    print("--------------------------------")
    print('quantas vezes aparece: Ana ->',lista.Conta('Ana'))
    print(lista.Busca("Antonio"))
    print("--------------------------------")
    lista.Adiciona("Ana")
    print(lista)
    print("--------------------------------")
    lista.Remove("Antonio")
    print(lista)
    print("--------------------------------")
  