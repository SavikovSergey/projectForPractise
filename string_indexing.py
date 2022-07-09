string = "a string"
def strings():
    print(string[0], string[2], string[-1], sep=",")

strings()
print(string[2:5])
print(string[:5])
print(string[2:])
print(string[::2])
print(string[::-1])

print(string[2] + string[-3:])
print(string[0] + string[1] + string[4:])