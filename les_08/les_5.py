# studenten = {}

# def namen():
#     while True:
#         studentnaam = input("Volgende naam: ")
#         naam = {"naam": studentnaam}

#         studenten.update(naam)
#         if studentnaam == '':
#             break

# namen()
# print(studenten)

studenten = {}
count = 0
studentenNaam = input("Volgende naam: ")
while studentenNaam != '':
    if studentenNaam in studenten:
        studenten[studentenNaam] = studenten[studentenNaam] + 1
    else:
        studenten[studentenNaam] = 1
    count = count + 1
    studentenNaam = input("Volgende naam: ")

    for k, v in studenten.items():
        print('Er zijn ' + str(v) + " studenten met de naam " + k)
