tableau1 =[]
tableau2 = []
n1 = int(input("Veuillez saisir un nombre entier positif pour la taille du tableau 1 : "))
for i in range(n1):
    element = int(input(f"Élément {i+1} : "))
    tableau1.append(element)
n2 = int(input("Veuillez saisir un nombre entier positif pour la taille du tableau 2 : "))
for i in range(n2):
    element = int(input(f"Élément {i+1} : "))
    tableau2.append(element)

tableau3 = []
k = 0
if len(tableau1) == len(tableau2):
    while k < len(tableau1):
        somme = tableau1[k]+tableau2[k]
        tableau3.append(somme)
        k +=1

elif len(tableau1)>len(tableau2):
    while k<len(tableau2):
        tableau3.append(tableau1[k]+tableau2[k])
        k+=1
    while k<len(tableau1):
        tableau3.append(tableau1[k])
        k+=1

else:
    while k<len(tableau1):
        tableau3.append(tableau1[k]+tableau2[k])
        k+=1
    while k<len(tableau2):
        tableau3.append(tableau2[k])
        k+=1

print(tableau3)

k=0
somme=k
while k<len(tableau3):
    somme+=tableau3[k]
    k += 1
moyenne=somme/len(tableau3)
print(moyenne)