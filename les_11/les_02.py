import json

bestand = open(
    "C:\\Users\\abuza\\OneDrive\\Documenten\\Programming\\les_11\\station.json")
data = json.load(bestand)

station = data['payload']

print("Dit zijn de namen, codes en types van elk station:")
for x in station:
    print('{:>25}  -{:>5} : {:>5}'.format(x['namen']['lang'],
                                          x['code'], x['stationType']))

y = 0
name = ""
for x in station:
    if x["lng"] > y:
        y = x["lng"]
        name = x['namen']['lang']

print("Het meest oostelijk gelegen station is:", name)
