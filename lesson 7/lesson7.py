class Human:
    def __init__(self, name):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self,human):
        self.passengers.append(human)

    def print_passenger(self):
        if self.passengers != []:
            print(f"name off {self.brand} passengers:")
            for i in self.passengers:
                print(i.name)
        else:
            print(f"There are no passenger in {self.brand}")

first_human = Human("Nick")
second_human = Human("Kate")

car = Auto("mersedes")
car.add_passenger(first_human)
car.add_passenger(second_human)
car.print_passenger()