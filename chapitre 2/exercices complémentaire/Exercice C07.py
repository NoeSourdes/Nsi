# -*- coding: utf-8 -*-
m=input("Donner un mot : ")
x=int(len(m)/2)
y=len(m)
if m==m[::-1]:
    print(m,"est un palindrome")
else:
    print(m,"n'est pas un palindrome")
