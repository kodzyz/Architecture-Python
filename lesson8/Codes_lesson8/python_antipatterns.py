# антипаттерны в Python

from os import unlink
from os.path import exists


class SomeException(Exception):
    pass

'''Возврат из функции переменных разных типов'''
# Bad: return должен возвращать значения одного типа
def some_func(arg):
    if not arg:
        return None
    return arg


res = some_func(None)

if res is not None:
    # go on
    pass

'''Обработка ошибок и исключительных ситуаций через if'''
# Good: нужно поднять свое исключение
def some_func(arg):
    if not arg:
        raise SomeException('no arg!')
    return arg


try:
    res = some_func(None)
    # go on
except SomeException:
    # handle it
    pass

nums = [1, 2, 3]

'''Создание словарей более сложным способом'''
# Bad: более сложный вариант чем возможно -> nums_squares2
nums_squares = dict([(elem, elem * 2) for elem in nums])

# Good
nums_squares2 = {elem: elem * 2 for elem in nums}

# Bad: валидация это всегда try - except
if exists("some_file.txt"):
    unlink("some_file.txt")

# Good
try:
    unlink("some_file.txt")
except OSError:
    pass

# Определение исключительной ситуации
# Это исключение?

'''Отдельное присваивание значений вместо распаковки'''
# Bad: потому что есть множественное присваивание
a = 15
b = 85

_tmp = a

a = b + 2
b = _tmp - 4

# Good

c = 15
d = 85

c, d = d + 2, c - 4

a, b, c = 1, 2, 3

data = 'leo:25'
name = data.split(':')[0]

name, _ = data.split(':')

nums = [10, 20, 30]

'''Использование map и фильтров вместо списковых включений'''
# Bad: более сложный путь
nums_proceed = map(lambda x: x * 2, nums)
print(list(nums_proceed))

# Good
nums_proceed2 = [x * 2 for x in nums]

# Bad: более сложный путь
nums_filtered = filter(lambda x: x < 10, nums)

# Good
nums_filtered2 = [x for x in nums if x < 10]