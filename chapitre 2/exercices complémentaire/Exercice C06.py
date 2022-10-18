# -*- coding: utf-8 -*-
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
