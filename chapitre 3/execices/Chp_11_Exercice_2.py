# -*- coding: utf-8 -*-
"""
NSI 1
Chapitre 11
exercice 2
"""
s=int(input("Combien de semaines avant les vacances ?"))
j=input("Quel jour de la semaine somme nous")
if j=='lundi'or'Lundi'or'1':
    j=1
if j=='mardi'or'Mardi'or'2':
    j=2
if j=='mercredi'or'Mercredi'or'3':
    j=3
if j=='jeudi'or'Jeudi'or'4':
    j=4
if j=='vendredi'or'Vendredi'or'5':
    j=5
if j=='samedi'or'Samedi'or'6':
    j=6
if j=='dimanche'or'Dimanche'or'7':
    j=7
r=(7-j)
r=s*7+r
print("Plus que ",r," jours avant les vacances !")

