class Student:
    print("Hi")
    amount_students = 0
    def __init__(self,name,health):
        self.health = health
        self.name = name
        self.lvl = 1
        print("I am alive!")
        Student.amount_students += 1

    def show(self):
        print(self.name)
        print(self.health)
        print(self.lvl)
    # How to Delete Student
    # Як видалити студента.
    def __del__(self):
        print("Student Deleted!")



First = Student(name=input("Enter Name: "),health=10)
First.show()

Second = Student(name="Kate",health=43)
Second.show()

Second.__del__()

Second.show()

print(Student.amount_students)