

class Person:
    d = {}
    def __init__(self, name: str, phone: int):
        self.name = name
        self.phone = phone
        Person.d[name] = phone
    
    @classmethod
    def remove_person(cls, name):
        Person.d.pop(name, None)

         
    @classmethod
    def data(cls):
        for k in Person.d.keys():
            print("Name: {0}, Phone: {1}".format(k, Person.d[k]))

p = Person("Max", 123)
p1 = Person("Eugene", 321)
p.data()
Person.remove_person("Max")
print()
Person.data()