# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 08:12:58 2022

@author: nsourdes
"""

#exemple 1: test simple
Temperature = int(input('Température maximale de la veille en °C ? '))

if Temperature > 30:
    print('Hier, il a fait chaud')
    print('Voire même très chaud')
    print("La chaleur était importante")    
    
Pluie =input('Cumul des précipitations de la veille en  mm ? ')


"""
Compléments:
Lancer l'exécution de l'exemple ci-dessus, SANS MODIFICATION.
Expliquer le résultat obtenu ICI :
    
    Le programme permet de demander la température, si la température est au dessus de 30 afficher certains message
    sinon afficher un autre message.
    
?????????????????????????????????

Modifier le code source pour le rendre opérationnel.
Tester votre code.

Compléter le code source pour que le message "La chaleur était importante" s'affiche
en plus des 2 autres messages (uniquement lorsque la température est > 30°). 
Tester votre code avec les valeurs de température 25° et 45° jusqu'à ce que le résultat
obtenu soit conforme à ce qui est demandé.
"""