import random
 
class Human:
    def __init__(self,name = "Human", job = None, home = None, car = None):
        self.name = name
        self.money = 100
        self.glendess = 50
        self.setiely = 50
        self.job = job
        self.home = home
        self.car = car
    
    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def chil(self):
        pass

    def clean_home(self):
        pass

    def days_index(self):
        pass

    def is_alive(self):
        pass

    def live(self):
        pass

class Auto:
    def __init__(self,brand_list):
        self.brand = random.choice(list(brand_list))
        self.color = brand_list[self.brand]["color"]

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Job:
    def __init__(self,job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.glandess_less = job_list[self.job]["gladness_less"]

brands_of_car = {
    "BWM": {"color":"Black"},
    "Lade": {"color":"Gray"},
    "Ferrari": {"color":"Yellow"},
    "Volvo": {"color":"Blue"},
}

job_list = {
    "Python Developer": {"salary":40,"glandess_less":3},
    "Teacher": {"salary":25, "glandess_less":25},
    "Game Developer": {"salary":35,"glandess_less":30},
}