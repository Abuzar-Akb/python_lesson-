invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

ConvertedList = invoer.split("-")
nummers = [int(x) for x in ConvertedList]

# print("Gesorteerde list van ints: ", nummers)

# Kleinste = min(nummers)
# Grootste = max(nummers)

# print("Grootste getal: ", Grootste, " en Kleinste getal: ", Kleinste)


# aantal = len(nummers)
# totaal = sum(nummers)

# print("Aantal getallen: ", aantal, " en Som van de getallen:", totaal)

# print("gemiddelde :", totaal/aantal)

# nummers = [int(nummer) for nummer in ConvertedList]
nummers = []
for nummer in ConvertedList:
    nummers.append(int(nummer))

print(nummers)
