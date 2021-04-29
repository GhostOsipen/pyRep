class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print("Hi", self.name)

p = Person("Max")
p.sayHi()