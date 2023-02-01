# (0:14)
class RegistryHolder(type):
    count = 0
    lst = []

    def __new__(cls, name, bases, attrs):
        '''перегрузка - при каждом описаним класса
        делаем изменение счетчика = + 1'''
        new_cls = type.__new__(cls, name, bases, attrs)

        '''
        <class '__main__.Animal'>
        <class '__main__.Bear'>
        <class '__main__.Cat'>
        class '__main__.Dog'>
        '''
        cls.count += 1  # каждый новый класс + 1 к счетчику
        cls.lst.append(new_cls.__name__)  # внесение каждого класса в массив
        return new_cls


class Animal(metaclass=RegistryHolder):
    count = 0

    def __init__(self):
        Animal.count += 1


class Bear(Animal):
    pass


class Cat(Animal):
    pass


class Dog(Animal):
    pass


print(RegistryHolder.lst)
