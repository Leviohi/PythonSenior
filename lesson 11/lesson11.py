for i in range(5):
  print(i+1)

my_list = [1,2,3]
iterator = iter(my_list)





print(next(iterator))
print(next(iterator))
print(next(iterator))

for i in iterator:
   print(i)


class Counter:
   def __init__(self,max_number):
       self.i = 0
       self.max_number = max_number
   def __iter__(self):
       self.i = 0
       return self
   def __next__(self):
       self.i += 1
       if self.i > self.max_number:
           raise StopIteration
       return self.i

c = Counter(10)

for i in c:
   print(i)

class Helper:
    def __init__(self, work):
        self.work = work
    def __call__ (self, work):
        return f"I will help you wth your {self.work}. After i will help you with {work}"

c = Helper("homework")
print(c("cleaning"))

