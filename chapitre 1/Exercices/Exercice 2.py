# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:36:21 2022

@author: jmaccallum
"""

RT = 6371000
G = 6.67e-11
mT = 6e24
h = int(input("Altitude : ",))
g = (G*mT)/(RT+h)**2
#déclaration et affectation des variables
print("L'accélération de la pésanteur à une altitude de",h,"m est",g,"m/s2")
#affichage des résultats