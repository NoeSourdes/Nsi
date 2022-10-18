# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:38:06 2022

@author: jmaccallum
"""

p=float(input("Quel est le prix hors taxes de votre article ? "))
t=float(input("Quel est le taux de TVA ? "))
c=p*(1+(t/100))
print("Le prix TTC de votre article est",c,"€")