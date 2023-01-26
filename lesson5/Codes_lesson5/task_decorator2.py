'''декораторы функций'''


def func_decorator(func):  # замыкание
    def wrapper():
        print("до вызова функции")
        func()
        print("после вызова функции")

    return wrapper


def some_func():
    print("вызов функции some_func")


# f --вызывает--> wrapper() --> some_func()
f = func_decorator(some_func)  # f = wrapper() ссылается на внутр функцию
f()
# до вызова функции
# вызов функции some_func
# после вызова функции

# обычно записывают так:
some_func = func_decorator(some_func)
some_func()

print(" ")


# с параметром

def func_decorator2(func):  # замыкание
    def wrapper(title):
        print("до вызова функции")
        func(title)
        print("после вызова функции")

    return wrapper


def some_func2(title):
    print(f"title={title}")


some_func2 = func_decorator2(some_func2)
some_func2("Python навсегда!")

# до вызова функции
# title=Python навсегда!
# после вызова функции

print(" ")


# много параметров - универсально

def func_decorator3(func):  # замыкание
    def wrapper(*args, **kwargs):
        print("до вызова функции")
        func(*args, **kwargs)
        print("после вызова функции")

    return wrapper


def some_func3(title, tag):
    print(f"title={title}, tag={tag}")


some_func3 = func_decorator3(some_func3)
some_func3("Python навсегда!", "h1")

# до вызова функции
# title=Python навсегда!, tag=h1
# после вызова функции

print(" ")


# когда 'some_func4' что-то возвращает: return

def func_decorator4(func):  # замыкание
    def wrapper(*args, **kwargs):
        print("до вызова функции")
        res = func(*args, **kwargs)
        print("после вызова функции")
        return res

    return wrapper


def some_func4(title, tag):
    print(f"title={title}, tag={tag}")
    return f"<{tag}>{title}</{tag}>"


some_func4 = func_decorator4(some_func4)
res = some_func4("Python навсегда!", "h1")
print(res)

# до вызова функции
# title=Python навсегда!, tag=h1
# после вызова функции
# <h1>Python навсегда!</h1>
