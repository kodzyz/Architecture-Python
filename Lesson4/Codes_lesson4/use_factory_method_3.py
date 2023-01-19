from factory_method_3 import Animal

'''Фабричный метод'''

animal_type = input()
animal = Animal.create_animal(animal_type)
animal.say()

#  cat
# мяу-мяу
