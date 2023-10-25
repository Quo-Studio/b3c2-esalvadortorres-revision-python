with open('file.txt', 'r') as file:
    content = file.read()
mots = content.split()

wordsCounter = len(mots)

with open('result.txt', 'w') as result:
    result.write("Nombre de mots : " + str(wordsCounter))

print("Ecriture terminée")
