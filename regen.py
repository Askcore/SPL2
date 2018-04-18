# regen.py
regnetEs = input("Regnet es(Ja/Nein)")
if (regnetEs == "Ja"):
    regen = True
    regenschirm = input("Hast du einen Regenschirm?")
    if(regenschirm == "Nein"):
        while (regen):
            print("Warte bis der Regen aufhört...")
            eingabe = input("Regnet es noch?(Ja/Nein) ")
            if (eingabe == "Nein"):
                regen = False
                print("Es hat aufgehört zu regnen...")
            elif (eingabe == "Ja"):
                print("Es regnet noch...")
            else:
                print("Es regnet noch")
print("Geh nach draussen Bursche...")
