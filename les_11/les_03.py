import json

lst = []

bestand = 'C:\\Users\\abuza\\OneDrive\\Documenten\\Programming\\les_11\\inloggers.json'

naam = ""

while True:
    naam = input("Wat is je achternaam? ")
    if naam == "einde":
        break
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")
    x = {
        "naam": naam,
        "voorl": voorl,
        "gbdatum": gbdatum,
        "email": email
    }
    lst.append(x)


with open(bestand, 'w+') as f:
    json.dump(lst, f)
