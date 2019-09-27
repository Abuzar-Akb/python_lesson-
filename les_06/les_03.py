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


# num_lines = sum(1 for line in open('kaartnummers.txt'))

# print("Deze file telt ", num_lines, " regels")

# integers = open('kaartnummers.txt', 'r')  # opens numbers.txt

# largestInt = 0  # making variables to store the largest/smallest int

# for line in integers:
#     values = line.split()
#     if largestInt <= int(values[0].strip().replace(',', '')):
#         largestInt = int(values[0].strip().replace(',', ''))

# integers.close()  # closes the file

# # print results
# print("Largest = ", largestInt)
