var = "global variable"

def function():
    print(var)

function()

print()

def function():
    print(var)

var = "global variable"
function()

print()

def function():
    var = "local variable"
    print(var)

var = "global variable"
function()
print(var)

print()

def function():
    global var
    var = "new variable"
    print(var)

var = "global variable"
function()
print(var)