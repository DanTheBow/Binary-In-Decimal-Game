from random import randint

# Hier wird das Spiel erklärt
print("Binary in Decimal Game:")
print("Die Aufgabe besteht darin Binärzahlen in Dezimalzahlen im Kopf umzurechnen")
print("Am Anfang wird gefragt wie viele Runden man spielen möchte")
print("Und wie hoch die zu erratene Binärzahl maximal sein soll")
print("Danach kommen die Binärzahlen, die man umrechnen soll")
print("Zum Schluss wird gezeigt wie viele man richtig umgerechnet hat")
print("Viel Spaß!")
print()

# Hier werden die Runden die gespielt werden sollen in einer Variable erfragt und gespeichert
counter = int(input("Gebe die Anzahl der Runden ein die du spielen möchtest: "))
# Hier wird gefragt wie hoch die zu erratene Binärzahl maximal sein soll
upper_bound = int(input("Wie hoch soll die zu erratene Binärzahl maximal sein ? "))
# Da wir am Ende die gespielten Runden sehen wollen wird die Rundenanzahl gespeichert
# Da wir die Variable Counter pro Runde ändern werden
tasks = counter
# In Right wird die Anzahl der richtigen Antworten gespeichert
right = 0


# Diese Funktion gibt uns mithilfe einer for-Schleife zufällige binäre Zahlen zwischen 0 und 15 zurück
def binarys():
    global counter
    global upper_bound
    for i in range(counter):
        binary = bin(randint(0, upper_bound))
        return binary


# Diese Schleife wird so lange
while counter > 0:
    value = binarys()  # Hier kommt die obere Funktion zum einsatz
    print(value)
    answer = int(input("In Dezimal: "))
    if value == bin(answer):  # Ist die Antwort richtig, erhöht sich right um 1
        right += 1
        print("Richtig")
        print()
    else:  # Sollte die Antwort falsch sein wird right nicht um 1 erhöht
        print("Falsch")
        print()
    counter -= 1  # Nach jedem Durchlauf wird der counter um 1 reduziert


# Hier wird das Ergebnis ausgegeben
print("Du hast " + str(right) + " von " + str(tasks) + " Aufgaben richtig gelöst!")
