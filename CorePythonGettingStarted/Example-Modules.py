


# Functions
def prtUpper(a):
    return(a.upper())

def prtLower(a):
    return(a.lower())

def prtTitle(a):
    return(a.title())

def prtCap(a):
    return(a.capitalize())

def myFunc(a, b):
    return a * b

a='Welcome Ramon'
print(prtUpper(a))
print(prtLower(a))
print(prtCap(a))
print(prtTitle(a))
x = myFunc(1, 5)
print(x)

print(__name__)