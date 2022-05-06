class Human:
    def __init__(self, name):
        self.name = name

class Hero:
    def __init__(self, hname):
        self.hname = hname
        self.heroes = []

    def add_heroes(self,human):
        self.heroes.append(human)

    def print_heroes(self):
        if self.heroes != []:
            print(f"Ім'я героїв {self.hname}:")
            for i in self.heroes:
                print(i.name)
        else:
            print(f"Немає героїв {self.hname}")

class Thief:
    def __init__(self, tname):
        self.tname = tname
        self.thieves = []

    def add_thieves(self,human):
        self.thieves.append(human)

    def print_thieves(self):
        if self.thieves != []:
            print(f"Ім'я злодіїв {self.tname}:")
            for i in self.thieves:
                print(i.name)
        else:
            print(f"Немає злодіїв {self.tname}")


first_hero = Human("Володимр Зеленський (Капітан Україна (Капітан Америка) )")
second_hero = Human("Віталій Кім (Залізний Українець (Залізна людина) )")
third_hero = Human("Арестович (Доктор Арестович (Доктор Стрендж) )")
fourth_hero = Human("Привид Києва(Український Яструб (Яструб) )")
fifth_hero = Human("Баба Надя(Українська Вдова (Чорна Вдова) )")
sixth_hero = Human("Циган, який вкрав танк(Циганос (Тансос) )")

first_thief = Human("володимир путін (Ху*ло!)")
second_thief = Human("кадиров (Загублений у часі)")
third_thief = Human("жириновський (Необержний дохляк)")
fourth_thief = Human("олександр лукашенко (Картопляний гад)")

car = Hero("в місті")
car.add_heroes(first_hero)
car.add_heroes(second_hero)
car.add_heroes(third_hero)
car.add_heroes(fourth_hero)
car.add_heroes(fifth_hero)
car.add_heroes(sixth_hero)
car.print_heroes()
car = Thief("в місті")
car.add_thieves(first_thief)
car.add_thieves(second_thief)
car.add_thieves(third_thief)
car.add_thieves(fourth_thief)
car.print_thieves()