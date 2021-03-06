import random
 
class Human:
    def __init__(self,name = "Human", job = None, home = None, car = None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.setiety = 50
        self.job = job
        self.home = home
        self.car = car
 
    def get_home(self):
        self.home  = House(house_list)
 
    def get_car(self):
        self.car  = Auto(brands_of_car)
 
    def get_job(self):
        self.job  = Job(job_list)
 
    def eat(self):
        if self.home.food <= 0:
            self.shopping(self)
        else:
            if self.setiety >=100:
                self.setiety = 100
            self.setiety += 5
            self.home.food -= 5
            self.setiety += 10
 
    def work(self):
        self.money += self.job.salary
        self.gladness -= self.job.glandess_less
        self.setiety -= 4
 
    def shopping(self,manage):
        if manage == "food":
            print("i bought food")
            self.money -= 50
            self.home.food += 30
 
    def chill(self):
        self.gladness += 10
        self.home.mess += 5
 
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
 
    def days_index(self,day):
        day = f"Today the {day} of {self.name}'s life"
        print(f"{day:=^50}")
 
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:=^50}","\n")
        print(f"Money - {self.money}")
        print(f"Gladness - {self.gladness}")
        print(f"Satiety - {self.setiety}")
 
        home_indexes = "Home Indexex"
        print(f"{home_indexes:=^50}","\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
 
 
 
    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.setiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrut...")
            return False
 
    def live(self,day):
        if self.is_alive() == False:
            return False
 
        if self.home is None:
            self.get_home()
            print(f"Settled in the house {self.home.name_house}")
 
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
 
        if self.job is None:
            self.get_job()
            print(f"Now i have a job {self.job.job} with salary {self.job.salary}")   
 
        self.days_index(day)
 
        dice = random.randint(1,3)
 
        if self.setiety < 20:
            print("i will go eat")
            self.eat()
 
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess...\n So i will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
 
 
 
class Auto:
    def __init__(self,brand_list):
        self.brand = random.choice(list(brand_list))
        self.color = brand_list[self.brand]["color"]
 
class House:
    def __init__(self,house_list):
        self.name_house = random.choice(list(house_list))
        self.type = house_list[self.name_house]["type"]
        self.food = 0
        self.mess = 0
 
class Job:
    def __init__(self,job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.glandess_less = job_list[self.job]["glendess_less"]
 
brands_of_car = {
    "BWM": {"color":"Black"},
    "Lade": {"color":"Gray"},
    "Ferrari": {"color":"Yellow"},
    "Volvo": {"color":"Blue"},
}
 
job_list = {
    "Python Developer": {"salary":40,"glendess_less":3},
    "Teacher": {"salary":25, "glendess_less":25},
    "Game Developer": {"salary":35,"glendess_less":30},
}
 
house_list = {
    "House": {"type":"House"},
    "Flat": {"type":"Flat"},
}
 
 
nick = Human(name = "Nick")
 
for day in range(360):
    if nick.live(day == False):
        break
    input("Press to continue...")

