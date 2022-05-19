import datetime
import gui_handler


def testTimeFormat(timeString):
    while True:
        try:
            finalTime = datetime.datetime.strptime(timeString, "%H:%M")
        except:
            timeString = input("Das Format ihrer Zeitangabe war fehlerhaft (HH:MM), bitte geben sie die Zeit erneut ein: ")
            continue
        break
    return finalTime

