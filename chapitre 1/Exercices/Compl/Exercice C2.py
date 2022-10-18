# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:00:10 2022

@author: jmaccallum
"""

print("Hello World ! ")
####################################################
#Rq : Histoire de Hello World
#https://fr.wikipedia.org/wiki/Hello_world
#https://fr.wikipedia.org/wiki/Brian_Kernighan
####################################################
Nom_Utilisateur = input("Quel est ton nom ? ")
print("Hello ",Nom_Utilisateur)
print("tu te nommes vraiment ",Nom_Utilisateur," ?")
Age_Utilisateur = int(input("Quel est ton age ? "))
A_de_n = 2019-Age_Utilisateur
print("Ton année de naissance est : ",A_de_n," ou ",A_de_n+1," ou ",A_de_n-1)
Taille_m_Util = float(input("Quel est ta taille en mètres ? "))
Taille_cm_Util = Taille_m_Util*100
print("tu mesure", Taille_cm_Util," cm") 