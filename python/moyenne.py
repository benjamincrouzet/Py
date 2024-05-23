tableau = []
n = int(input("Veuillez saisir un nombre entier positif pour la taille du tableau : "))
for i in range(n):
    element = float(input(f"Élément {i+1} : "))
    tableau.append(element)

k=0
somme=k
while k<len(tableau):
    somme+=tableau[k]
    k += 1
moyenne=somme/len(tableau)
print(moyenne)