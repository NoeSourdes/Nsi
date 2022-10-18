# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 08:50:30 2022

@author: nsourdes
"""

print('Table de multiplication par 2:')
print()
for i in range(3):
    for j in range(4):
        print('2 x',4*i + j + 1,' = ',2*(4*i + j + 1),'\t',end='')
    print()
    print()

print('Table de multiplication par 8:')
print()
for i in range(5):
    for j in range(3):
        print('8 x',3*i + j + 1,' = ',8*(3*i + j + 1),'\t\t',end='')
    print()
    print()
print('Table de multiplication par 5:')
print()
for i in range(5):
    for j in range(3):
        print('5 x',3*i + j + 1,' = ',5*(3*i + j + 1),'\t\t',end='')
    print()


"""
Compléments:
En vous inspirant du code ci-dessus, écrire le code qui affiche la table de multiplication 
par 5 (de 5 x 1 à 5 x 12).

En vous inspirant du code ci-dessus, écrire puis tester le code qui affiche EXACTEMENT la 
table de multiplication par 8 suivante:
    
Table de multiplication par 8:

8 x 1  =  8 		   8 x 2  =  16 		   8 x 3  =  24 		
8 x 4  =  32 		   8 x 5  =  40 		   8 x 6  =  48 		
8 x 7  =  56 		   8 x 8  =  64 		   8 x 9  =  72 		
8 x 10  =  80 		   8 x 11  =  88 		   8 x 12  =  96 		
8 x 13  =  104 		8 x 14  =  112 		8 x 15  =  120 	


"""
