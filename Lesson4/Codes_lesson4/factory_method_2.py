from abc import ABC, abstractmethod

'''Фабричный метод'''


#  Цель – есть некоторая иерархия объектов
# и мы хотим не зависеть от конкретики в клиентском коде.

class Animal(ABC):

    @abstractmethod
    def say(self):
        pass


class Dog(Animal):

    def say(self):
        print('wow-wow')


class Cat(Animal):

    def say(self):
        print('мяу-мяу')


class Bird(Animal):

    def say(self):
        print('мяу-мяу')


class AnimalCreator:

    @staticmethod
    def create_animal(animal_type):
        '''
        Нам предлагается создание объекта животного
        перенести в отдельный класс.
        '''
        if animal_type == 'dog':
            animal = Dog()
        elif animal_type == 'cat':
            animal = Cat()
        elif animal_type == 'bird':
            animal = Bird()

        return animal
