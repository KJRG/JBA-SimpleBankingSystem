class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return "Hello, I am {}!".format(self.name)


input_name = input()
person = Person(input_name)
print(person.greet())
