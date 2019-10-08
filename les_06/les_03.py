nummerLines = sum(1 for line in open('kaartnummers.txt'))

print("Deze file telt ", nummerLines, " regels")

maxNummer = 0
LineCount = 1
with open('kaartnummers.txt', 'r') as inFile:
    for lijn in inFile:
        nummer = int(lijn.split(',')[0])
        if nummer > maxNummer:
            maxNummer = nummer
            LineNummer = LineCount
        LineCount += 1


print("Het grootste kaartnummer is:", maxNummer,
      "en dat staat op regel", LineNummer)
