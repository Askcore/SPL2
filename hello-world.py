
print ("Hallo, Ich bin ein Computer namens AlexbertaCorones")
name = input("Wie ist dein Name? ")
print ("Schön dich zu treffen ", name ,". Dein Name ist ", len(name) ," Zeichen lang.", sep="")

alter = input ("Wie alt bist du? ")
alter = int(alter)
if(alter > 100):
    print ("Du willst mich doch verarschen du alter Trottel, oder?")
else:
    print ("Du wirst in einem Jahr ", alter+1 ," Jahre alt!", sep="")
print ("Tschüdele...")

