# Поток лавы (Lava flow)
# # Одна часть кода написана с учетом ошибки в другой части кода

# В этом примере первый разработчик допустил ошибку в функции,
# второй – написал свою с учетом этой ошибки,
# третий – с учетом ошибки второго и т.д.

def cities():
    result = ['gelendzik', 'piter', 'tula', 1, 'perm', 'samara']
    return result


def double():
    city_list = cities()
    return [item * 2 for item in city_list]


print(double())
