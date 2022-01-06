#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:51:04 2021

@author: lyliana
"""
hash_table = [None] * 13

def hash1(item, hash_table):
    M = len(hash_table)
    s = 0
    # s conterá a soma dos valores numéricos dos caracteres
    for chr in item:
        s = s + ord(chr)
    return s % M # valor da função

def hash2(item, hash_table):
    M = len(hash_table)
    s = 0
    # s conterá a soma dos valores numéricos dos caracteres
    for chr in item:
        s = s + ord(chr)
    return (3 - s) % M # valor da função

def search(hash_table, item):
    M = len(hash_table)
    h1 = hash1(item, hash_table)
    h2 = hash2(item, hash_table)
    for i in range(len(hash_table)):
        if str(hash_table[(h1 + i * h2) % M][0]) == str(item):
            return (h1 + i * h2) % M


def double_hashing(hash_table, item, position):
    M = len(hash_table)
    h1 = hash1(item, hash_table)
    h2 = hash2(item, hash_table)
    for i in range(len(hash_table)):
        if hash_table[(h1 + i * h2) % M] is None:
            hash_table[(h1 + i * h2) % M] = [item,position]
            break
        if hash_table[(h1 + i * h2) % M][0] == item:
            hash_table[(h1 + i * h2) % M] == hash_table[(h1 + i * h2) % M].append(position)
            

double_hashing(hash_table, 'senizio',1)
double_hashing(hash_table, 'lorentao',2)
double_hashing(hash_table, 'romulo',3)
double_hashing(hash_table, 'oscaran',4)
double_hashing(hash_table, 'lorentao',5)
TAB_HASH = []
item = input("search: ")
if not search(hash_table, item) == None:
    print("index of searched item is: {}".format(search(hash_table, item)))
else:
    print("Not Found!")
print(hash_table)