# Function
def f1():
    a = 1
    b = 2
    c = a + b
    print(c)


f1()


# Function Parameter
def f2(a, b):
    c = a + b
    print(c)


f2(1, 2)


# Function parameter order
def f3(a, b):
    print(a, b)


f3(1, 2)
f3(b=1, a=2)


# Function return value
def f4(a, b):
    c = a + b
    return c


c = f4(1, 2)
print(c)