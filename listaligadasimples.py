#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 16:37:44 2021

@author: lyliana
"""
class SinglyLinkedList:
    
    class _Node:
        
        slots = '_element' , '_next'
         
        def init (self, element, prox):
            self._element = element
            self._prox = prox
       
        def __str__(self):
                    
            return str(self._element)
    
#---------Implementação dos métodos de pilha----------

    def __init__(self):
        
        self._head = None
        self._size = 0
    
    def __len__(self):
        
        return self._size == 0 
    
    def is_empty(self):
        
        return self._size == 0
    
    def push(self, e):
        #adiciona no topo da lista
        self._head = self._Node(e, self._head)
        self._size += 1
        
    def pop(self):
        #remove o elemento do topo da lista
        
        if self.is_empty():
            raise ValueError('A lista ta vazia')
            
        answer = self._head._element
        self._head = self._head._prox
        self._size -= 1
        
        return answer
    
    def __str__(self):
        # Mostra os elementos da lista duplamente ligada, mostrando também o anterior e o sucessor.
        valor = ''
        percorre = self._head
        while percorre:
              
                valor += str(percorre._head)
                percorre = percorre._prox
                    
        return valor
    
if __name__ == "__main__":
    # Programa teste exemplo da classe ListaDuplamenteLigada
    lx = SinglyLinkedList()
    print(lx)
    lx.push(12)
    print(lx)