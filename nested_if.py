x = float(input("x = "))

if 0 < x < 7 :
    print("Value is in range, let`s continue")
    y = 2 * x -5
    if y < 0:
        print("y is negative")
    else:
        if y > 0:
            print("y is positive")
        else:
            print("y = 0")

print()

x = float(input("x = "))

if 0 < x < 7 :
    print("Value is in range, let`s continue")
    y = 2 * x -5
    if y < 0:
        print("y is negative")
    elif y > 0:
            print("y is positive")
    else:
            print("y = 0")
else:
    if x < 0:
        print("X is not in range ")
    elif x > 7:
        print("X is not in range ")

print()

x = float(input("x = "))
y = float(input("y = "))
oper = input("Enter a operation: ")
if oper == "+" :
    print(x+y)
elif oper == "-" :
    print(x-y)
elif oper == "/" :
    print(x/y)
elif oper == "*" :
    print(x * y)
else: print("Enter a right operation")
