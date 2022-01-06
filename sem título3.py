#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:41:37 2021

@author: lyliana
"""
class Duplas:
    '''Define a classe Duplas.'''
    # Construtor da classe
    def __init__(self, p1 = 0, p2 = 0):
        '''Construtor da classe.'''
        self.primeiro = p1
        self.segundo = p2
    # Retorna no primeiro parâmetro a soma de dois elementos da classe
    def SomaDuplas(self, d1, d2):
        self.primeiro = d1.primeiro + d2.primeiro
        self.segundo = d1.segundo + d2.segundo
    # Mostre uma dupla no formato /a b/
    def Mostre(self):
        print("/", self.primeiro, self.segundo, "/")

# Exemplos de uso da classe
# /3 4/
x = Duplas(3, 4)
x.Mostre()
# /2 0/
y = Duplas(2)
y.Mostre()
# /0 0/
z = Duplas()
z.Mostre()
# z = x + y
z.SomaDuplas(x, y)
z.Mostre()
# z = /5 8/ + /1 1/
z.SomaDuplas(Duplas(5, 8), Duplas(1, 1))
z.Mostre()
