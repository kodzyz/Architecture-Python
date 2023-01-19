from abc import ABC, abstractmethod

'''Фабричный метод'''


# базовый класс
class Animal(ABC):  # абстрактное животное

    @abstractmethod
    def say(self):  # умеет говорить
        pass


# наследники
class Dog(Animal):

    def say(self):
        print('wow-wow')


# наследники
class Cat(Animal):

    def say(self):
        print('мяу-мяу')
