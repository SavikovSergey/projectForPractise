attempt_left = 3
while attempt_left > 0:
    attempt_left -= 1
    password = input("Enter your password (you have {} attempt left): ".format(attempt_left+1))
    if password == "fbc35":
        print("Access granted")
        break
else:
    print("Passwords are not right. Access denied")
