def nonrecursive_factorial(n):
    result = 1
    for multiplier in range(2, n + 1):
        result *= multiplier
    return result
a = int(input("Enter a number: "))
print(nonrecursive_factorial(a))

print()

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return  n * recursive_factorial(n-1)

b = int(input("Enter a number: "))
print(nonrecursive_factorial(b))
