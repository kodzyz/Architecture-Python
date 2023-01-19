from factory_method_4 import Animal

'''Фабричный метод'''

animal_type = input()
animal = Animal.create_animal(animal_type)
animal.say()

#  dog
# wow-wow
