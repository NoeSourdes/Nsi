# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:27:10 2022

@author: jmaccallum
"""

a=float(input("Donne moi ta dernière note : "))
x=float(input("Donne moi le coefficient de ta dernière note : "))
b=float(input("Donne moi ton avant dernière note : "))
y=float(input("Donne moi le coefficient de ton avant dernière note : "))
c=float(input("Donne moi ton avant avant dernière note : "))
z=float(input("Donne moi le coefficient de ton avant avant dernière note : "))
d=(a*x+b*y+c*z)/(x+y+z)
print("La moyenne de :")
print(" -votre dernière note ",a," coef ",x)
print(" -votre avant dernière note ",b," coef ",y)
print(" -votre avant avant dernière note ",c," coef ",z)
print("est ",d)
