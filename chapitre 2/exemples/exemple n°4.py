# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 08:25:50 2022

@author: nsourdes
"""

Temperature = float(input('Température maximale de la veille en °C ? '))
if Temperature > 30:
    print('Hier, il a fait chaud')
    print('Voire même très chaud')  
elif Temperature >= 20:
    print('Hier, la température a été supportable')
    print("Il faisait pas trop chaud")
else:
    print("Hier, la température n'était pas très élevée")
Pluie = float(input('Cumul des précipitations de la veille en  mm ? '))

"""
Compléments:
Tester le code ci-dessus avec les valeurs de température de 15°, 20°, 25°, 30° et 35°.

Compléter le code source, sans rajouter de "if ...", pour que le message "Il faisait 
pas trop chaud" s'affiche en plus du message initial, lorsque la température est comprise
entre 20° et 30°. 
Tester votre code avec les valeurs de température 15°, 25° et 35° jusqu'à ce que le 
résultat obtenu soit conforme à ce qui est demandé.
    
"""