from abc import ABC, abstractmethod

'''Фабричный метод'''


#  Смысл в том,
# что мы вытащим метод create_animal()
# и положим его в абстрактный класс.
# Теперь Animal создает своих потомков сам.

class Animal(ABC):

    @abstractmethod
    def say(self):
        pass

    @staticmethod
    def create_animal(animal_type):
        if animal_type == 'dog':
            animal = Dog()
        elif animal_type == 'cat':
            animal = Cat()
        return animal


class Dog(Animal):

    def say(self):
        print('wow-wow')


class Cat(Animal):

    def say(self):
        print('мяу-мяу')
