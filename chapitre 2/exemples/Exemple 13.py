# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 08:34:36 2022

@author: jmaccallum
"""

#exemple 13 Version 1 : 
print("exemple 13")
nombre = int(input('Saisir un nombre: '))
somme = 0
i = 0
while i < nombre:
    if (i%2)!=0:
        somme += i
    i = i + 1
print(somme)
