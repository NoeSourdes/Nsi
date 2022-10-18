# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 08:34:16 2022

@author: nsourdes
"""

s = 0
for i in range(5):
    s = s + i
    print('La variable s vaut: ',s)
print()
print()
s = 0
for i in range(8):
    s = s + i
    print('La variable s vaut: ',s)
print()
print()
s = 0
for i in range(9):
    s = s + i
    print('La variable s vaut: ',s)

"""
Compléments:
Compléter le code source pour afficher les valeurs successives de s 
après chaque itération de la boucle. 
Tester le code ainsi modifié. Justifier chacune des valeurs de s affichées.

Version 2 : Modifier le code source initial pour que la boucle fasse la somme des 8 premiers entiers. 
Tester le code ainsi modifié jusqu'à ce que le résultat soit correct (=28).

Version 3 : Modifier le code source initial pour que la boucle fasse 
la somme des 8 premiers entiers non nuls.
Tester le code ainsi modifié jusqu'à ce que le résultat soit correct (=36).

"""