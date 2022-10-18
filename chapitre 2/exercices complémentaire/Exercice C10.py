# -*- coding: utf-8 -*-
#A
a=int(input("Donner le nombre de lignes : "))
for i in range(1,a+1):
    print("*"*i)

#B
b=int(input("Donner le nombre de lignes : "))
for i in range(1,2*a+1,2):
    print("*"*i)

#C
c=int(input("Donner le nombre de lignes : "))
x=1
while x<c/2:
    print("*"*x)
    x=x+1
if c%2==0:
    print("*"*(c//2))
while x>0:
    print("*"*x)
    x=x-1
