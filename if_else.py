x = float(input("x = "))
if x > 0:
    y = pow(x,0.5)
else :
    y = pow(x,2)

print(y)

print()

name = input("Enter your name: ")

if name == "Sergey":
    print("You have entered", name)
    print("This is my name, too.")
    print("Welcome to my house,", name)
else:
    print("Your name differs from mine.")
