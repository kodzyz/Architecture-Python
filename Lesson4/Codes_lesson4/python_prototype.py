'''питоновский Прототип'''
#  есть некоторый большой объект,
#  который уже наполнен данными и нам быстрее его скопировать,
#  нежели создать новый

# модуль copy
from copy import deepcopy


class Original:
    pass


original = Original()
prototype = deepcopy(original)

prototype.name = 2
