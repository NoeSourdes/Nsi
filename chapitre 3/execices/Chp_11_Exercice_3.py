# -*- coding: utf-8 -*-
"""
NSI 1
Chapitre 11
exercice 3
"""
"""
Salut bob g un pb sur le code suivant pour la spécification :
    
détection du palindrome, avec une boucle while par 
comparaison des lettre symétriques.
Tant que les lettres sont identiques et que les indices ne se croisent pas,
la boucle avance.
Quand on est sorti de la boucle on détecte le palindrome avec les indices.

Pour l'instant cela ne marche pas,
tu me le déplante stp asap

jeux de test :
"kayak" -> est un palindrome
"radar" -> est un palindrome
"ressasser" ->   est un palindrome
"palindrome" -> n'est pas un palindrome
"pythonnade" -> n'est pas un palindrome
"suis" -> n'est pas un palindrome
"""
m=input("donne un mot :")
n=1
nn=len(m)
while m[n]!=m[nn] and nn<n:  
    n+=-1
    nn-=-1
if  nn>n :
    print(nn," est un palindrome")
else :     
    print(n," n'est pas un palindrome")