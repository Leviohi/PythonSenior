def f(x):
    return x * 2

result = f(2)
print(result)

result = f(int(input("enter number")))
print(result)

def k(a, b, c):
    return a + b + c

number = k(int(input("enter number")),int(input("enter number")), int(input("enter number")))
print(number)

def num(x):
    return x * 2

result = num(int(input("enter number")))

if result > 10:
    print(str(result) + " > 10")
else:
    print(str(result) + " < 10")