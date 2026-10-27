password = input("Enter password: ")

if (len(password) >= 8
    and any(c.isupper() for c in password)
    and any(c.islower() for c in password)
    and any(c.isdigit() for c in password)
    and any(not c.isalnum() for c in password)):

    print("Valid Password")

else:
    print("Invalid Password")
