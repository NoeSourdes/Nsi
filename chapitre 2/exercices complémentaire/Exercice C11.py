# -*- coding: utf-8 -*-
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
