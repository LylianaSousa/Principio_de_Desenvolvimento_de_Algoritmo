#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 16:38:17 2021

@author: lyliana
"""
class ListaDuplamenteLigada:
''' operações sobre uma lista duplamente ligada. '''
# classe _Node - interna
class _Node:
__slots__ = '_info', '_prev', '_prox'
def __init__ (self, info, prev, prox):
# inicia os campos
self._info = info
self._prev = prev
self._prox = prox

def __str__(self):
                
                return str(self._info)
# métodos de lista duplamente ligada
def __init__ (self):
''' cria uma lista circular vazia.'''
self._inicio = self._Node(None, None, None) # vazia
self._final = self._Node(None, None, None) # vazia
self._inicio._prox = self._final
self._final._prev = self._inicio
self._tamanho = 0 # tamanho da lista
def __len__(self):
''' retorna o tamanho da pilha.'''
return self._tamanho
def is_empty(self):
''' retorna True se pilha vazia'''
return self._tamanho == 0
def adicionar_entre(self, e, anterior, sucessor):
''' adiciona elemento entre 2 outros.
retorna o novo nó.'''
novo = self._Node(e, anterior, sucessor)
anterior._prox = novo
sucessor._prev = novo
self._tamanho += 1
return novo
def remove(self, node):
''' remove nó da lista e retorna seu valor.'''
anterior = node._prev
sucessor = node,_prox
anterior._prox = sucessor
sucessor._prev = anterior
self._tamanho -= 1
val = node._info # guarda a informação
# inative o nó
node._prev = node._prox = node._info = None
return val