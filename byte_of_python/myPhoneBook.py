import pickle

class Person:
    d = {}
   
    @classmethod
    def delete_person_by_name(cls, name: str):
        del Person.d[name]
        print(name, "deleted")

    @classmethod
    def add_person(cls, name: str, phone: int):
        Person.d[name] = phone

    @classmethod
    def change_person_name(cls, oldName, newName):
        Person.d[newName] = Person.d[oldName]
        del Person.d[oldName]
        oldName = newName
        print("changed")

    @classmethod
    def change_person_phone(cls, name, newPhone):
        Person.d[name] = newPhone
        print("changed")
         
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

while True:
    s = input()
    if s == "exit":
        break
    if s == "table":
        Person.data()
    if s == "add":
        print("input name =>")
        name = input()
        print("input phone =>")
        phone = input()
        Person.add_person(name, phone)
    if s == "delete":
        print("input name =>")
        Person.delete_person_by_name(name = input())
    if s == "change":
        print("what do you wanna change? =>")
        change = input()
        if change == "name":
            print("old name =>")
            old_name = input()
            print("new name =>")
            new_name = input()
            Person.change_person_name(old_name, new_name)
        elif change == "phone":  
            print("name =>")
            name = input()
            print("new phone =>")
            new_phone = input()
            Person.change_person_phone(name, new_phone)
    if s == "find":
        print("find by name or phone? =>")
        find = input()
        if find == "name":
            print("input name =>")
            Person.find_by_name(s = input())
        if find == "phone":
            print("input phone = >")
            Person.find_by_phone(s = input())

    if s == "save":
        print("save to data.pickle...")
        with open('data.pickle', 'wb') as f:
            pickle.dump(Person.d, f)
    if s == "load":
        print("load from data.pickle...")
        with open('data.pickle', 'rb') as f:
            Person.d = pickle.load(f)

    if s == "help":
        print('''exit   <= to exit
table  <= data list
add    <= add person
delete <= remove person
change <= change person
find   <= find someone
save   <= to data.pickle
load   <= load from data.pickle
help   <= for help!''')
