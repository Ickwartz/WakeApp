import datetime

#prepTime = input("Wie lange brauchen sie um sich vor dem los gehen fertig zu machen: ")
additionalDelay = 0


def getTimeOfArrival():
    ankunftszeit = input("Geben Sie bitte Ihre gewünschte Ankunftszeit ein(HH:MM): ")
    
    while True:
        try:
            datetime.datetime.strptime(ankunftszeit, "%H:%M")
        except:
            ankunftszeit = input("Das Format ihrer Zeitangabe war fehlerhaft (HH:MM), bitte geben sie die Zeit erneut ein: ")
            continue
        break
    return ankunftszeit

print(getTimeOfArrival())