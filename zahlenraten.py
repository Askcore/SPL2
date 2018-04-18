import random
z2 = input("Geben sie das Maximum ein: ")
z2 = int(z2)

zufallszahl = random.randint(1, z2)

fertig = False
versuche = 0

while(fertig == false)
    zEingabe = input("Geben sie eine Zahl zwischen 1 und", z2 ,"ein:")
    versuche +=1
    if(zEingabe)