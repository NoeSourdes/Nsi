# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 08:16:41 2022

@author: nsourdes
"""

Temperature = float(input('Température maximale de la veille en °C ? '))
if Temperature > 30:
    print('Hier, il a fait chaud')
    if Temperature > 40:
        print('La température était excessive')
        if Temperature > 50:
            print("La chaleur était insupportable")
Pluie = float(input('Cumul des précipitations de la veille en  mm ? '))


"""
Compléments:
Tester le code ci-dessus avec les valeurs de température de 25°, 35° et 45°.

Compléter le code source pour que le message "La chaleur était insupportable" s'affiche
en plus des 2 autres messages, uniquement s'il fait plus de 50°. 
Tester votre code avec les valeurs de température 35°, 45° et 55° jusqu'à ce que le 
résultat obtenu soit conforme à ce qui est demandé.
"""