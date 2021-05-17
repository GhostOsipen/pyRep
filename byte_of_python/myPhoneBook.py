import pickle

class Person:
    def __init__(self,  name, last_name, phone) -> None:
        self.name = name
        self.phone = phone
        self.last_name = last_name

        print(f"{self.name} ADDED")

    def __del__(self) -> None:
        pass

class PhoneBook:
    d = {}

    @classmethod
    def add_person(cls, name: str, last_name: str, phone: str):
        person = Person(name, last_name, phone)
        cls.d[person.name] = person

    @classmethod
    def delete_person_by_name(cls, name: str):
        del cls.d[name]
        print(name, "DELETED")

    @classmethod
    def change_person_name(cls, old_name, new_name):
        cls.d[old_name].name = new_name
        cls.d[new_name] = cls.d[old_name]
        del cls.d[old_name]
        print("CHANGED")

    @classmethod
    def change_person_last_name(cls, name, new_last_name):
        cls.d[name].last_name = new_last_name
        print("CHANGED")

    @classmethod
    def change_person_phone(cls, name, new_phone):
        cls.d[name].phone = new_phone
        print("CHANGED")

    @classmethod
    def person_list(cls):
        for person in cls.d.values():
            print(f"Name: {person.name}, Second name: {person.last_name}, Phone: {person.phone}")

    @classmethod
    def find_person(cls, s):
        for person in cls.d.values():
            if (s.lower() in person.name.lower()) or (s.lower() in person.last_name.lower()) or (s.lower() in person.phone.lower()):
                print(f"Name: {person.name}, Second name: {person.last_name}, Phone: {person.phone}")


print("Hello there!")

while True:
    command = input().split()

    if len(command) == 1:
        if command[0] == "exit":
            break
        elif command[0] == "table":
            PhoneBook.person_list()
        elif command[0] == "change":
            print("what do you wanna change? (name, second name, phone) =>")
            change = input()
            if change == "name":
                print("old name =>")
                old_name = input()
                print("new name =>")
                new_name = input()
                PhoneBook.change_person_name(old_name, new_name)
            elif change == "second name":
                print("name =>")
                name = input()
                print("new second name =>")
                new_last_name = input()
                PhoneBook.change_person_last_name(name, new_last_name)
            elif change == "phone":
                print("name =>")
                name = input()
                print("new phone =>")
                new_phone = input()
                PhoneBook.change_person_phone(name, new_phone)
        elif command[0] == "save":
            print("save to data.pickle...")
            with open('data.pickle', 'wb') as f:
                pickle.dump(PhoneBook.d, f)
        elif command[0] == "load":
            print("load from data.pickle...")
            with open('data.pickle', 'rb') as f:
                PhoneBook.d = pickle.load(f)
        elif command[0] == "help":
            print('''exit   <= to exit
table  <= data list
add    <= add PhoneBook
delete <= remove PhoneBook
change <= change PhoneBook
find   <= find someone
save   <= to data.pickle
load   <= load from data.pickle
help   <= for help!''')

    if len(command) == 2:
        if command[0] == "delete":
            PhoneBook.delete_person_by_name(name=command[1])
        elif command[0] == "find":
            PhoneBook.find_person(command[1])

    if len(command) == 3:
        if command[0] == "add":
            PhoneBook.add_person(command[1], "-", command[2])

    if len(command) == 4:
        if command[0] == "add":
            PhoneBook.add_person(command[1], command[2], command[3])
