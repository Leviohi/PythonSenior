class Hero:
    print("Hi")
    amount_heros = 0
    def __init__(self,name,health,age,power,race):
        self.health = health
        self.name = name
        self.age = age
        self.power = power
        self.race = race
        print("I am alive!")

    def show(self):
        print(self.name)
        print(self.health + " здоров'я")
        print(self.age + " років")
        print(self.power + " рівень сили")
        print(self.race)
    # How to Delete Student
    # Як видалити студента.
    def __del__(self):
        print("Hero Deleted!")


print("В расі вибирати тількі: Варвар, Ельф, Лицар, Лучник, Маг, Гоблін, Козак і Вершник.")
print("В силі писати цифрами рівень сили.")
First = Hero(name=input("Enter name: "), race=input("Enter race: "), power=input("Enter power: "), age=input("Enter age: "), health=input("Enter health: "))
First.show()

print("В расі вибирати тількі: Варвар, Ельф, Лицар, Лучник, Маг, Гоблін, Козак і Вершник.")
print("В силі писати цифрами рівень сили.")
Second = Hero(name=input("Enter name: "), race=input("Enter race: "), power=input("Enter power: "), age=input("Enter age: "), health=input("Enter health: "))
Second.show()

print("В расі вибирати тількі: Варвар, Ельф, Лицар, Лучник, Маг, Гоблін, Козак і Вершник.")
print("В силі писати цифрами рівень сили.")
Third = Hero(name=input("Enter name: "), race=input("Enter race: "), power=input("Enter power: "), age=input("Enter age: "), health=input("Enter health: "))
Third.show()

print("В расі вибирати тількі: Варвар, Ельф, Лицар, Лучник, Маг, Гоблін, Козак і Вершник.")
print("В силі писати цифрами рівень сили.")
Fourth = Hero(name=input("Enter name: "), race=input("Enter race: "), power=input("Enter power: "), age=input("Enter age: "), health=input("Enter health: "))
Fourth.show()

print("В расі вибирати тількі: Варвар, Ельф, Лицар, Лучник, Маг, Гоблін, Козак і Вершник.")
print("В силі писати цифрами рівень сили.")
Fifth = Hero(name=input("Enter name: "), race=input("Enter race: "), power=input("Enter power: "), age=input("Enter age: "), health=input("Enter health: "))
Fifth.show()

print("В расі вибирати тількі: Варвар, Ельф, Лицар, Лучник, Маг, Гоблін, Козак і Вершник.")
print("В силі писати цифрами рівень сили.")
Sixth = Hero(name=input("Enter name: "), race=input("Enter race: "), power=input("Enter power: "), age=input("Enter age: "), health=input("Enter health: "))
Sixth.show()

print("В расі вибирати тількі: Варвар, Ельф, Лицар, Лучник, Маг, Гоблін, Козак і Вершник.")
print("В силі писати цифрами рівень сили.")
Seventh = Hero(name=input("Enter name: "), race=input("Enter race: "), power=input("Enter power: "), age=input("Enter age: "), health=input("Enter health: "))
Seventh.show()

print("В расі вибирати тількі: Варвар, Ельф, Лицар, Лучник, Маг, Гоблін, Козак і Вершник.")
print("В силі писати цифрами рівень сили.")
Eighth = Hero(name=input("Enter name: "), race=input("Enter race: "), power=input("Enter power: "), age=input("Enter age: "), health=input("Enter health: "))
Eighth.show()