# -*- coding: utf-8 -*-
import turtle as tu
tu.up()
tu.goto(-450, 0)
tu.down()
x = 30
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
    x = x+10
