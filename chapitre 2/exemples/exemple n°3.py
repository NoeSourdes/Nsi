# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 08:19:49 2022

@author: nsourdes
"""

Temperature = float(input('Température maximale de la veille en °C ? '))
if Temperature > 30:
    print('Hier, il a fait chaud')
    print('Voire même très chaud')    
else:
    print('Il faisait plutôt bon')
    print('Hier, la température a été supportable')
Pluie = float(input('Cumul des précipitations de la veille en  mm ? '))


"""
Compléments:
Tester le code ci-dessus avec les valeurs de température de 25°, 35° et 45°.

Compléter le code source, sans rajouter de "if ...", pour que le message "Il faisait 
plutôt bon" s'affiche en plus du message initial, lorsque la température est <= 30°. 
Tester votre code avec les valeurs de température 25°, 30° et 35° jusqu'à ce que le 
résultat obtenu soit conforme à ce qui est demandé.
    
"""
