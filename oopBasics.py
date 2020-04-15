class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self,num):
        print("I am an Dog")

test = Dog()
test.who_am_i(1)
Animal.who_am_i(test)


