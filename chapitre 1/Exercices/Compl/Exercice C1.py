# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 08:33:54 2022

@author: jmaccallum
"""
x=float(input("Nombre : "))
if x<0:
    print("Calcul impossible car valeur négative")
elif (x-int(x)) !=0:
        print("Ce nombre n'est pas un nombre entier")
else:
    a=x**(1/2)
    print("ça fait",a)    
