import time


def test_time(func):  # замыкание
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы: {dt} сек")
        return res

    return wrapper


# Алгоритм Евклида для нахождения НОД
@test_time  # декорируем авто
def get_nod(a, b):  # найбольший общий делитель
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time  # декорируем авто
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


# декорируем вручную
# get_nod = test_time(get_nod)
# get_fast_nod = test_time(get_fast_nod)

res = get_nod(2, 100000)
res2 = get_fast_nod(2, 100000)
print(res, res2)

# Время работы: 0.0044519901275634766 сек
# Время работы: 2.1457672119140625e-06 сек
# 2 2
