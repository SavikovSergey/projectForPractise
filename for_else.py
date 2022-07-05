attempt_left = 3
for attempt_left in range(3,0,-1):
    password = input("Enter your password (you have {} attempt left): ".format(attempt_left))
    if password == "fbc35":
        print("Access granted")
        break
else:
    print("Passwords are not right. Access denied")
