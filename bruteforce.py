password = int(input("Entrez le code: "))
code = " "
for i in range(1001): 
    print(f"Tentative avec le mot de passe {i:03d}") 

    if i == password: 
        code = i
        print("***********************************")
        print(f"Le mot de passe trouvé est {code:03d}")  #rempli des 0 à gauche tant que la taille de code n'est pas égale à 3
        break
else:
    print("Mot de passe non trouvé")
