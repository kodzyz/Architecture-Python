from abc import ABC, abstractmethod

'''Фабричный метод'''


#  избавляемся от if...else

class Animal(ABC):

    @abstractmethod
    def say(self):
        pass

    @staticmethod
    def create_animal(animal_type):
        ANIMALS = {
            'dog': Dog,
            'cat': Cat,
            'bear': Bear
        }
        return ANIMALS[animal_type]()


class Dog(Animal):

    def say(self):
        print('wow-wow')


class Cat(Animal):

    def say(self):
        print('мяу-мяу')


class Bear(Animal):

    def say(self):
        print('мяу-мяу')
