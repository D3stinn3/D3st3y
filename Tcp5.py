"""object oriented programing"""
import random

class Pet:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def show(self):

        print(f'Name : {self.name} Age: {self.age}')

    def speak(self):

        message = ['Sasa', 'Hi', 'Uko Aje', 'Hello']

        random_message = random.choice(message)

        print(f'Name : {self.name} Message : {random_message}')

class Dog(Pet):

    def __init__(self, name, age, color):

        self.name = name

        super().__init__(name, age) # this acts on behalf of the super class Dog and as an instance
        self.color = color

    def show(self):

        print(f'Name : {self.name} Age : {self.age} Color : {self.color}')

    def speak(self):

        message = ['Bark', 'GRR', 'wof']

        random_message = random.choice(message)

        print(f'Name: {self.name} Message : {random_message}')


mbwa_wetu = Dog('Loki', 15, 'Green')
mbwa_wetu.show()
mbwa_wetu.speak()

class Person:

    number_of_people = 0

    def __init__(self, name):

        self.name = name
        Person.add_person()

    @classmethod    
    def number_of_people_(cls): # the cls in this instance is the normal self method for any class method
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person('Destinne')
p2 = Person('Jill')
p3 = Person('Fally')

print(Person.number_of_people_())







