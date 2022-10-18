# 1)
x = int(input("Donner le minimum : "))
y = int(input("Donner le maximum : "))
z = float(input("Donner le pas : "))
print("x", "\t\t", "y=x^2-x+3", "\t\t", "y")
p = (y-x)//z+1
while x < y+z:
    print(x, "\t\t", "(", x, ")^2-(", x, ")+3", "\t\t", x*x-x+3)
    x = x+z
