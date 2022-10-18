# 1)
nb1 = int(input("Donne moi un nombre ? : "))
nb2 = int(input("Donne moi un deuxième nombre ? : "))
if nb1 < nb2:
    print("Ton deuxième nombre est plus grand")
else:
    print("Ton premier nombre est plus grand")
print()
print()

# 2)
nb1 = int(input("Donne moi un nombre ? : "))
nb2 = int(input("Donne moi un deuxième nombre ? : "))
nb3 = int(input("Donne moi un troisième nombre ? : "))
if nb1 < nb2 and nb2 > nb3:
    print("Ton deuxième nombre est plus grand")
if nb1 > nb2 and nb1 > nb3:
    print("Ton premier nombre est plus grand")
else:
    print("Ton troisième nombre est plus grand")
print()
print()

# 3)
nombredenombrechoisiparutilisateur = int(
    input("Combien veut tu choisir de nombre : "))
conteur = 0
conteur2 = 0
conteur3 = 0
while conteur < nombredenombrechoisiparutilisateur:
    nb = int(input("Donne moi un nombre : "))
    conteur = conteur+1
    conteur3 = nb
    if conteur3 > conteur2:
        conteur2 = nb
print("ton nombre le plus grans est", conteur2)
