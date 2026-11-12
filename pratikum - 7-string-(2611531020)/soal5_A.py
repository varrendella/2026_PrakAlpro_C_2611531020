username = input("username: ")

if len(username) < 5:
    print("invalid: at least 5 character")
elif not username.isalnum():
    print("invalid: letters and digits only")
elif not username[0].isalpha():
    print("invalid: must start with a letter")
else:
    print("valid")