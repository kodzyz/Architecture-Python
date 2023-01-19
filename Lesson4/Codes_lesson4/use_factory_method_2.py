from factory_method_2 import AnimalCreator

'''Фабричный метод'''
# Теперь модулю use_factory_method_2.py
# вообще не нужно знать про типы животных.
# Он знает только про AnimalCreator.
# А AnimalCreator где-то внутри себя знает,
# какого типа животное нужно создать.
animal_type = input()
animal = AnimalCreator.create_animal(animal_type)
animal.say()

#  dog
# wow-wow
