oldpassword = "abu123"


def new_password(oldpassword, newpassword):
    # len(newpassword) < 5 and

    if oldpassword == newpassword:
        return "het wachtwoord mag niet het zelfde zijn"
    elif len(newpassword) < 6:
        return "wachtwoord moet langer dan 6 charaters"
    elif any(chacater.isdigit() for chacater in newpassword) == False:
        return "wachtwoord moet een min 1 cijfer"
    else:
        oldpassword = newpassword
        return True


newpassword = input("wachtwoord veranderen : ")

print(new_password(oldpassword, newpassword.lower()))
