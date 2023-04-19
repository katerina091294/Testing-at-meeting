class Animal:

    def __init__(self, animal_type, __nickname, age, height, weight):
        self.animal_type = animal_type
        self.__nickname = None
        self.age = age
        self.height = height
        self.weight = weight

    def set_nickname(self, nickname):
        self.__nickname = nickname

    def get_nickname(self):
        return self.__nickname

    def eat(self):
        print(f'{self.animal_type} can eat =)')

    def sleep(self):
        print(f'{self.animal_type} can sleep =)')

    def sound(self):
        print(f'{self.animal_type} can talk =)')


# creating instances (dog) of the class Animal
dog = Animal('Dog', 'Bobik', 3, 10, 0.65)  # we cannot assign name this way if variable is private, use set method
dog.eat()
dog.sleep()
dog.sound()
print(dog.__dict__)
print(dog.get_nickname())
dog.set_nickname('Bobik')
print(dog.get_nickname())
