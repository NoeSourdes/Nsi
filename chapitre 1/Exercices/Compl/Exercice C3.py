# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:17:45 2022

@author: jmaccallum
"""
a=float(input("Donne moi ta dernière note : "))
b=float(input("Donne moi ton avant dernière note : "))
c=float(input("Donne moi ton avant avant dernière note : "))
d=(a+b+c)/3
print("La moyenne de :")
print(" -votre dernière note ",a)
print(" -votre avant dernière note ",b)
print(" -votre avant avant dernière note ",c)
print("est ",d)
