

class Person:
    d = {}
    def __init__(self, name: str, phone: int):
        self.name = name
        self.phone = phone
        Person.d[name] = phone
    
    def __del__(self):
        Person.d.pop(self.name, None)

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
import toga


def add_handler(sender):
    print("hello")

def del_handler(widget):
    print("hello")

def build(app):
    box = toga.Box()

    add_person_cmd = toga.Command(
        add_handler,
        label="Add person",
        tooltip="Add person tooltip")



    table = toga.Table(['Name', 'Phone'])
    table.style.padding = 10
    table.style.flex = 1

    # add_button = toga.Button('Hello world', on_press=add_button_handler)
    # add_button.style.padding = 10
    # add_button.style.flex = 1

    # del_button = toga.Button('Hello world', on_press=del_button_handler)
    # del_button.style.padding = 10
    # del_button.style.flex = 1

    # box.add(add_button)
    # box.add(del_button)
    box.add(table)

    app.main_window.toolbar.add(add_person_cmd)

    return box


def main():
    return toga.App('Phone Book', '1', startup=build)


if __name__ == '__main__':
    main().main_loop()