a = float(input("donne moi une valeur pour a : "))
b = float(input("donne moi une valeur pour b : "))
c = float(input("donne moi une valeur pour c : "))
delta = b**2-4*a*c
if delta < 0:
    print("pas de solution !!")
elif delta == 0:
    print("Une seul solution !!")
else:
    print("Deux solution !!")
