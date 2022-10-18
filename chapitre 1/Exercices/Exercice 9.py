# -*- coding: utf-8 -*-
a=int(input("donnez-moi votre avant dernière note"))
b=int(input("donnez-moi votre avant avant dernière note"))
c=int(input("donnez-moi votre avant avant avant dernière note"))
d=int(input("donnez-moi votre avant avant avant avant dernière note"))
print("la moyenne de vos notes est",(a+b+c+d)/4)

a,b,c,d = input("Donnez-moi vos quatre dernières notes").split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
print("la moyenne de vos notes est",(a+b+c+d)/4)