
studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(studentencijfers):

    antw = [sum(row)/len(row) for row in studentencijfers]

    return antw


def gemiddelde_van_alle_studenten(studentencijfers):

    antw = [sum(row)/len(studentencijfers) for row in zip(*studentencijfers)]
    return antw

    # antw = [sum(row)/2 for row in studentencijfers]
    # return antw


print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))
