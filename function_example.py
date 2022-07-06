def print_numbers(limit):
    for i in range(limit):
        print(i)

n = int(input("n="))
print_numbers((n))

print()

def increase(number):
    number += 1

x = 8
increase(x)
print(x)

print()

def increase(number):
    print("Number was", number)
    number += 1
    print("Number became", number)

x = 8
increase(x)