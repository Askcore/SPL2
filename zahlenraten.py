import random
z2 = input("Geben sie das Maximum ein: ")
z2 = int(z2)

zufallszahl = random.randint(1, z2)

fertig = False
versuche = 0
zEingabe = 0

while(fertig == False):
    print("Geben sie eine Zahl zwischen 1 und", z2 ,"ein:", end="")
    zEingabe = input()
    zEingabe = int(zEingabe)
    versuche +=1
    if(zEingabe == zufallszahl):
        fertig = True
        print("Du hast", versuche ,"Versuche gebraucht.")