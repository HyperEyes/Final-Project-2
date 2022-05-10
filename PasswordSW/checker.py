import re
def password_checker(password):
    while True:

        newpass = len(password)

        if not newpass >= 11:
            print("The password is too short.")
            break
        if not re.search("[a-z]", password):
            print("The password is missing a lower case letter!")
            break
        elif not re.search("[A-Z]", password):
            print("Your password is missing an upper case letter!")
            break
        elif not re.search("[0-9]", password):
            print("You password is missing a number!")
            break
        elif not re.search("[?!@#$%&]", password):
            print("You are missing a symbol.")
            break
        else:
            print("The password is strong!")
            break

password_checker("AZAMER1@LLLL")