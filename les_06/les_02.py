qbfile = open("kaartnummers.txt", "r")

# hoe krijg ik de , weg
for aline in qbfile:
    values = aline.split()
    print(values[1], 'heeft kaartnummer: ', values[0].replace(',', ''))

qbfile.close()
