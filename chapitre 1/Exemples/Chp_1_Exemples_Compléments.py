# -*- coding: utf-8 -*- 

"""
Éditeur de Spyder

@author: merle
"""
#exemple 0
# symbole dièse : une ligne en commentaire

""" 3 guillemets double
des lignes de commentaires
des lignes de commentaires
"""

''' 3 guillemets simple
des lignes de commentaires
des lignes de commentaires
'''

################################################################
#exemple 1
""" # supprimer cette ligne (et sa ligne jumelle) pour pouvoir interpréter le bloc de code suivant

a=1 # la variable a reçoit la valeur 1 : a <-- 1
b=2 # la variable b reçoit la valeur 2 : b <-- 2

print('le calcul de a+b donne :',a+b)

""" # supprimer cette ligne (et sa ligne jumelle) pour pouvoir interpréter le bloc de code précédent

################################################################
#exemple 2
""" # supprimer cette ligne (et sa ligne jumelle) pour pouvoir interpréter le bloc de code suivant

a=2 # la variable a reçoit la valeur 2 : a <-- 2
b=3 # la variable   
a=7 # la variable   
A=5 # Les variables A et a sont ???

print("la variable a contient la valeur : ",a)
print("la variable b contient la valeur : ",b)
print("la variable A contient la valeur : ",A)

""" # supprimer cette ligne (et sa ligne jumelle) pour pouvoir interpréter le bloc de code précédent

"""
compléments :   ajouter un commentaire # d'explication pour les affectations des variables b, a et A.
                créer une variable B et affecter lui la valeur 33, ajouter un commentaire # d'explication
                afficher à l'écran la valeur de la variable B, avec une présentation identique aux autres affichages
"""

################################################################
#exemple 3
"""
a=1
b=1
print()

a,b=3,4
print()

a,b=b,a
print()
"""
"""
complément :    Compléter les différents print() par l'affichage du résultat du calcul a-b, et d'une phrase de présentation
                ajouter un commentaire # d'explication pour chaque affectation.

"""
################################################################
#exemple 4
"""
c=a+b
d=b-a
e=a*b
f=a/b
g=a//b
h=a%b
i=a**b

print("la variable c contient la valeur : ",c)
print("la variable d contient la valeur : ",d)
print("la variable e contient la valeur : ",e)
print("la variable f contient la valeur : ",f)
print("la variable g contient la valeur : ",g)
print("la variable h contient la valeur : ",h)
print("la variable i contient la valeur : ",i)

"""
"""
complément :    ajouter un commentaire # d'explication pour chaque calcul et affectation.
"""

################################################################
#exemple 5
"""

j=2*3+2     # La multiplication est prioritaire (2*3)+2
k=2*(3+2)   # Les parenthèses s’emploient comme sur une calculatrice.
l=1+3**2    # L'élévation à la puissance s'écrit ** en python 
            # Le calcul d’une puissance est prioritaire sur les autres opérations 1+(3**2)

print("la variable j contient la valeur : ",j)
print("la variable k contient la valeur : ",k)
print("la variable l contient la valeur : ",l)
"""
"""
complément :    ???
"""

################################################################
#exemple 6
"""
a=2
b=3
f=a/b
print(" ??? ",type(a))
print(type(b))
print(type(f))

print(id(a))
print(id(b))
print(id(f))
print(id(z))
"""
"""
complément :    Completer les différents print() par l'affichage d'une phrase de présentation
                créer une variable g et affecter lui le résultat du calcul de a à la puissance b
                afficher à l'écran la valeur de la variable g
                afficher à l'écran le type   de la variable g
                afficher à l'écran l'adresse de la variable g
"""


################################################################
#exemple 7
"""
a=2
b=3
print('a = ',a,' b = ',b)
print()



"""
"""
complément :    Ajouter un commentaire # d'explication pour expliquer
                l'utilisation de la  fonction print() vide !?
                Completer le code pour tester et afficher les différences entre l'opérateur = et le test ==
                ajouter un commentaire # d'explication pour chaque ligne.

"""
################################################################
#exemple 8
"""
k=1.5e-2
print('k = ',k)
j=1.5*10**-2
print('j = ',j)

"""
"""
complément :    Ajouter un commentaire # d'explication pour monter les points communs aux deux exemples précédents
                Completer le code pour : 
                    affecter la variable m avec la valeur : 5,6 
                    affecter la variable p avec la valeur : 7
                    affecter la variable q avec le résultat du calcul : m multiplié par 10^(-p)
                    afficher à l'écran les valeurs et les types des variables m,p,q
                    vérifier à la calculatrices le résultat.
                ajouter un commentaire # d'explication sur les priorités de calculs.

"""

################################################################
#exemple 9
"""
a=5
a=2*a
print('a = ',a)
a=a+2
print('a = ',a)
a=4
a*=2
print('a = ',a)
a=a+2
print('a = ',a)

"""
"""
complément :    Ajouter un commentaire # d'explication pour monter les points communs aux deux exemples précédents
                Completer le code pour : 
                    affecter la variable m avec la valeur : 5,6 
                    affecter la variable p avec la valeur : 7
                    affecter la variable q avec le résultat du calcul : m multiplié par 10^(-p)
                    afficher à l'écran les valeurs et les types des variables m,p,q
                    vérifier à la calculatrices le résultat.
                ajouter un commentaire # d'explication sur les priorités de calculs.

"""
################################################################
#exemple 10
"""
a,b,c = 4,2,1
print('???',a<b)
print('???',b>c)
d=a<b
print('???',d)
type ('??? : ',R)
e=(b>c)
print('???',e)
type ('??? : ',e)

"""
"""
complément :    Ajouter des commentaires # d'explication pour les lignes précédentes
                Completer le code pour : 
                    afficher à l'écran un texte cophérent en remplacement des '??? :'
"""
################################################################
#exemple 11
"""
nom=input('Nom de ton lycée ? ')
print('Le nom de ton lycée est :',nom)
type ('??? : ',nom)
id   ('??? : ',nom)

"""
"""
complément :    Ajouter des commentaires # d'explication pour les lignes précédents
                Completer le code pour : 
                    afficher à l'écran un texte cophérent en remplacement des '??? :'
"""
################################################################
#exemple 12
"""
age=input('Quel est ton âge ? ')
print('??? :',age)
type ('??? :',age)
id   ('??? :',age)
"""
"""
age=int(age)
print('??? :',age)
type ('??? :',age)
id   ('??? :',age)
"""
"""
age=int(input('Quel est ton âge ? '))
print('??? :',age)
type ('??? :',age)
id   ('??? :',age)
"""
"""
complément :    Ajouter un commentaire # d'explication pour monter les points communs aux deux exemples précédents
                Completer le code pour : 
                    affecter la variable m avec la valeur : 5,6 
                    affecter la variable p avec la valeur : 7
                    affecter la variable q avec le résultat du calcul : m multiplié par 10^(-p)
                    afficher à l'écran les valeurs et les types des variables m,p,q
                    vérifier à la calculatrices le résultat.
                ajouter un commentaire # d'explication sur les priorités de calculs.

"""
################################################################
#exemple 13
"""
taille=input('Quel est ta taille en m ? ')
print('??? :',taille)
type ('??? :',taille)
id   ('??? :',taille)
"""
"""
taille=float(taille)
print('??? :',taille)
type ('??? :',taille)
id   ('??? :',taille)
"""
"""
age=float(input('Quel est ta taille en m ? '))
print('??? :',taille)
type ('??? :',taille)
id   ('??? :',taille)
"""
"""
complément :    Ajouter un commentaire # d'explication pour monter les points communs aux deux exemples précédents
                Completer le code pour : 
                    affecter la variable m avec la valeur : 5,6 
                    affecter la variable p avec la valeur : 7
                    affecter la variable q avec le résultat du calcul : m multiplié par 10^(-p)
                    afficher à l'écran les valeurs et les types des variables m,p,q
                    vérifier à la calculatrices le résultat.
                ajouter un commentaire # d'explication sur les priorités de calculs.

"""




