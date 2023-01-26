'''Замыкания в Python '''


def say_name(name):
    def say_goodbye():
        print(f"Don't say goodbye, {name}!")

    return say_goodbye


f = say_name('Sergey')  # ссылка на say_goodbye потому что она return внешней
f()  # Don't say goodbye, Sergey!

f2 = say_name('Python')  # создаются два независимых лок окружения
f2()  # Don't say goodbye, Python!


def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step  # внешняя ф-я должна вернуть внутреннюю


# независимые счетчики
c1 = counter(10)
c2 = counter()
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())


# 11 1
# 12 2
# 13 3

def strip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


strip1 = strip_string()  # strip1 = do_strip(string)
strip2 = strip_string(" !?,.;")
print(strip1(" hello python!.. "))  # do_strip( hello python!.. ) # hello python!..
print(strip2(" hello python!.. "))  # hello python
