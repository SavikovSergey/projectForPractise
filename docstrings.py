# print(print.__doc__)

def function():
    """  Пример функции
    Строка, стоящая в самом начале функции, -- это документационная строка.
    """
    print("function called")

function()
help(function)

print(function.__doc__)