# -*- coding: utf-8 -*-
#boucle for
x=int(input("Donner un nombre entier : "))
y=0
print(x,"est divisible par",end=" ")
for i in range(1,x):
    if x%i==0:
        y=y+1
        print(i,end=" ")
print("et lui-même,",end=" ")
if y==1:
    print("c'est donc un nombre premier")
else:
    print("ce n'est donc pas un nombre premier")

#boucle while
x=int(input("Donner un nombre entier : "))
a=1
y=0
print(x,"est divisible par",end=" ")
while a!=x:
    if x%a==0:
        y=y+1
        print(a,end=" ")
    a=a+1
print("et lui-même,",end=" ")
if y==1:
    print("c'est donc un nombre premier")
else:
    print("ce n'est donc pas un nombre premier")
