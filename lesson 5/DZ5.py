def max(x, y):
    if x > y:
        return x
    elif y > x:
        return y
result = max(int(input("Enter number: ")), int(input("Enter number: ")))
print(result)

def lenght(l):
    return len(l)
leng = lenght(input("Enter sentence: "))
print(leng)

def num(a, b, c):
    return (a + b + c) / 3
math = num(int(input("Enter number: ")), int(input("Enter number: ")), int(input("Enter number: ")))
print(math)

def month(m):
    if m == 1:
        return "Січень"
    elif m == 2:
        return "Лютий"
    elif m == 3:
        return "Березень"
    elif m == 4:
        return "Квітень"
    elif m == 5:
        return "Травень"
    elif m == 6:
        return "Червень"
    elif m == 7:
        return "Липень"
    elif m == 8:
        return "Серпень"
    elif m == 9:
        return "Вересень"
    elif m == 10:
        return "Жовтень"
    elif m == 11:
        return "Листопад"
    elif m == 12:
        return "Грудень"
    else:
        return "Error"
print("Пишіть цифри від 1 до 12")
mon = month(int(input("Enter number: ")))
print(mon)

    