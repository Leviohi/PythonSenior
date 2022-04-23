class Student:
    print("Hi!")
    def __init__(self,name, age):
        self.name = name
        self.age = age
        print("I an alive")
    def show(self):
            print(self.age)
            print(self.name)
first_student = Student(name=input ("Enter name "), age=60)
first_student.show()

second_student = Student(name="Kate", age= 1)
second_student.show()
