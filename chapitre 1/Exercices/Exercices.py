# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 08:34:25 2022

@author: jmaccallum
"""
print("Exercice 1")
nb1 = 125 
#on déclare et affecte la variable nb1 avec la valeur 125
nb2 = 1.25 
#on déclare et affecte la variable nb2 avec la valeur 1,25
nb3 = 12 
#on déclare et affecte la variable nb3 avec la valeur 12
nb4 = nb1+nb2 
#on calcule la somme nb1+nb2 et place le résultat dans la variable nb4
nb5 = nb1//nb3
#on calcule le quotient de la division euclidienne de nb1 par nb3 et place le résultat dans la variable nb5
nb6 = nb1%nb3
#on calcule le reste de la division euclidiennede nb1 par nb3 et place le résultat dans la variable nb6
print("nb1 =",nb1,", nb2 =",nb2,", nb3 =",nb3)
print("la somme de nb1 et nb2 vaut",nb4)
print("nb1 puissance 12 fait",nb1**nb3)
print("le quotient de la division euclidienne de nb1 par nb2 fait",nb5)
print("le reste de la division euclidienne de nb1 par nb2 fait",nb6)
print("les types de nb5 et nb6 sont",type(nb5),"et",type(nb6))
print("les adresses mémoire de nb5 et nb6 sont",id(nb5),"et",id(nb6))
#affichage des résultats
print("")
print("**********************************************************************")
print("")
print("Exercice 2")
RT = 6371000
G = 6.67e-11
mT = 6e24
h = int(input("Altitude : ",))
g = (G*mT)/(RT+h)**2
#déclaration et affectation des variables
print("L'accélération de la pésanteur à une altitude de",h,"m est",g,"m/s2")
#affichage des résultats
print("")
print("**********************************************************************")
print("")
print("Exercice 3")
print("")
print("**********************************************************************")
print("")