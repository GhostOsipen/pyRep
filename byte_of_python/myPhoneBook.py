

class Person:
    d = {}
    def __init__(self, name: str, phone: int):
        self.name = name
        self.phone = phone
        Person.d[name] = phone
    
    def __del__(self):
        Person.d.pop(self.name, None)

    # @classmethod
    # def remove_person(cls, name):
    #     Person.d.pop(name, None)

    def change_person_name(self, newName):
        Person.d[newName] = Person.d[self.name]
        del Person.d[self.name]
        self.name = newName
    
    def change_person_phone(self, newPhone):
        Person.d[self.name] = newPhone
         
    @classmethod
    def data(cls):
        for k in Person.d.keys():
            print("Name: {0}, Phone: {1}".format(k, Person.d[k]))

    @classmethod
    def find_by_name(cls, s):
        for k in Person.d.keys():
            if s in k:
                print("Name: {0}, Phone: {1}".format(k, Person.d[k]))

    @classmethod
    def find_by_phone(cls, s):
        for k in Person.d.keys():
            if str(s) in str(Person.d[k]):
                print("Name: {0}, Phone: {1}".format(k, Person.d[k]))



p = Person("Max", 123)
p1 = Person("Eugene", 321)
Person.data()

del p1
print()
Person.data()

p.change_person_name("Mox")
print()
Person.data()

p.change_person_phone(111)
print()
Person.data()

p1 = Person("Eugene", 321)
print()
print("find")
Person.find_by_name("Mo")
Person.find_by_phone(1)

#===================
