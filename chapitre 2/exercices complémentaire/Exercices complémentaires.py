# -*- coding: utf-8 -*-

#Exercice 1     test: 1 et 2 ; 2 et 1
a=float(input("Donner un nombre : "))
b=float(input("Donner un autre nombre : "))
if a>b:
    print("Le premier nombre",a,"est plus grand que le second",b)
else:
    print("Le second nombre",b,"est plus grand que le premier",a)

#Exercice 2     test: 2, 3 et 5 ; 2, 3 et 1 ; 4, 8, 4
a=float(input("Donner la valeur de a : "))
b=float(input("Donner la valeur de b : "))
c=float(input("Donner la valeur de c : "))
d=b*b-4*a*c
if d<0:
    print("Pas de solution")
elif d==0:
    print("Une seule solution")
else:
    print("Deux solutions")

#Exercice 3     test: 5, 46, 2
x=int(input("Donner le minimum : "))
y=int(input("Donner le maximum : "))
z=float(input("Donner le pas : "))
print("x","\t\t","y=x^2-x+3","\t\t","y")
p=(y-x)//z+1
while x<y+z:
    print(x,"\t\t","(",x,")^2-(",x,")+3","\t\t",x*x-x+3)
    x=x+z

#Exercice 4     test: 4
x=int(input("Donner le nombre de termes : "))
print("U 0","\t\t","  0")
a=0
for j in range(x):
    print("U",j+1,"\t","3 *",a,"+ 1 =",3*a+1)
    a=3*a+1

#Exercice 5     test: bon, jour ; bonjour, rond
a=input("Donner une chaîn de caractèrese : ")
b=input("Donner une autre chaîne de caractères : ")
if b[0]==a[-1]:
    print(a)
else:
    print(a+b)

#Exercice 6     test: 2022
x=int(input("Quelle année est-il ? "))
if x%4==0:
    if x%100==0:
        if x%400==0:
            print("L'année",x,"est une année bissextile")
            print("Les trentes prochaines années bissextiles sont ",end="")
            for j in range (x,x+120,4):
                print(j+4,end=" ")
        else:
            print("L'année",x,"n'est pas une année bissextile")
            print("Les trentes prochaines années bissextiles sont ",end="")
            for i in range(1,4):
                if (i+x)%4==0:
                    if (i+x)%100==0:
                        if (i+x)%400==0:
                            for j in range (i+x,i+x+120,4):
                                print(j,end=" ")
                    else:
                        for j in range (i+x,i+x+120,4):
                            print(j,end=" ")
    else:
        print("L'année",x,"est une année bissextile")
        print("Les trentes prochaines années bissextiles sont ",end="")
        for j in range (x,x+120,4):
            print(j+4,end=" ")
else:
    print("L'année",x,"n'est pas une année bissextile")
    print("Les trentes prochaines années bissextiles sont ",end="")
    for i in range(1,4):
        if (i+x)%4==0:
            if (i+x)%100==0:
                if (i+x)%400==0:
                    for j in range (i+x,i+x+120,4):
                        print(j,end=" ")
            else:
                for j in range (i+x,i+x+120,4):
                    print(j,end=" ")

#Exercice 7     test: radar ; pomme
m=input("Donner un mot : ")
x=int(len(m)/2)
y=len(m)
if m==m[::-1]:
    print(m,"est un palindrome")
else:
    print(m,"n'est pas un palindrome")

#Exercice 8     test: 23:06:59, 01:02:00 ; 24:60:00, 00:60:01
départ=input("Saisir l'horraire de départ sous le fomat HH:MM:SS : " )
hd=int(départ[0:2])
md=int(départ[3:5])
sd=int(départ[6:8])
if départ[2]!=":" or départ[5]!=":" or hd>24 or md>60 or sd>60:
    print("Entrée invalide")
else:
    arrivée=input("Saisir l'horraire d'arrivée sous le fomat HH:MM:SS : " )
    ha=int(arrivée[0:2])
    ma=int(arrivée[3:5])
    sa=int(arrivée[6:8])
    if arrivée[2]!=":" or arrivée[5]!=":" or ha>24 or ma>60 or sa>60:
        print("Entrée invalide")
    else:
        if hd==24:
            hd=0
        if md==60:
            md=0
        if sd==60:
            sd=0
        if ha==24:
            ha=0
        if ma==60:
            ma=0
        if sa==60:
            sa=0
        xs=0
        a=False
        while sd!=sa:
            sd=sd+1
            xs=xs+1
            if sd==60:
                a=True
                sd=0
        if a==True:
            md=md+1
        xm=0
        a=False
        while md!=ma:
            md=md+1
            xm=xm+1
            if md==60:
                a==True
                md=0
        if a==True:
            hd=hd+1
        xh=0
        a=False
        while hd!=ha:
            hd=hd+1
            xh=xh+1
            if hd==24:
                hd=0
        secondes=xh*3600+xm*60+xs
        if xh<10:
            strh="0"+str(xh)
        else:
            strh=str(xh)
        if xm<10:
            strm=":0"+str(xm)
        else:
            strm=":"+str(xm)
        if xs<10:
            strs=(":0"+str(xs))
        else:
            strs=":"+str(xs)
        print("La durée du trajet est de",strh+strm+strs,"soit",secondes,"secondes")   

#Exercice 9     test: 27 ; 23
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

#Exercice 10     test: 6 ; 5
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

#Exercice 11     test: carré ; triangle ; hexagone ; exemple
import turtle as tu
x=input("Préférez-vous le carré, le triangle ou l'hexagone : ")
#1
if x=="carré":
    for a in range(4):
        tu.forward(150)
        tu.right(90)
#2
elif x=="triangle":
    for b in range(3):
        tu.forward(150)
        tu.right(240)
#3
elif x=="hexagone":
    for c in range(6):
        tu.forward(50)
        tu.right(60)
else:
    for a in range(4):
        tu.forward(150)
        tu.right(90)
    tu.up()
    tu.goto(-200)
    tu.down()
    for b in range(3):
        tu.forward(150)
        tu.right(240)
    tu.up()
    tu.goto(200)
    tu.down()
    for c in range(6):
        tu.forward(50)
        tu.right(60)

#Exercice 12
import turtle as tu
tu.up()
tu.goto(-450,0)
tu.down()
for i in range(10):
    for j in range(4):
        tu.forward(50)
        tu.left(90)
    tu.up()
    tu.forward(55)
    tu.down()

#Exercice 13
import turtle as tu
tu.up()
tu.goto(-450,0)
tu.down()
x=30
for i in range(7):
    for j in range(4):
        tu.forward(x)
        tu.right(90)
    tu.up()
    tu.forward(x+5)
    tu.down()
    for k in range(3):
        tu.forward(x)
        tu.right(120)
    tu.up()
    tu.forward(x+5)
    tu.down()
    x=x+10
