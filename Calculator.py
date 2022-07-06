print("The first calculator")
n = float(input("Enter a first number: "))
m = float(input("Enter a second number: "))
oper = input("Enter an operation: ")
if oper == "+":
    print(n+m)
elif oper == "-":
    print(n-m)
elif oper == "*":
    print(n*m)
elif oper == "/":
    print(n/m)
else:
    print("Incorrect operation")

print("The second calculator")

a = float(input("Enter a first number: "))
oper = input(""" Select an operation
1. "+"
2. "-"
3. "*"
4. "/"
""")
b = float(input("Enter a second number: "))
if oper == "1":
    print(a+b)
elif oper == "2":
    print(a-b)
elif oper == "3":
    print(a*b)
elif oper == "4":
    print(a/b)
else:
    print("Incorrect operation")

print("The third calculator")

x = float(input("First number: "))
y = float(input("Second number: "))
operation = input("Operation: ")

result = None

if operation == "+":
    result = x + y
elif operation == "-":
    result = x - y
elif operation == "*":
    result = x * y
elif operation == "/":
    result = x / y
else:
    print("Unsupported operation")
if result is not None:
    print("Result:", result)
