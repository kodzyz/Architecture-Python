# proproprogs.ru
# класс для работы с БД
# в программе должен существовать
# только один экземпляр этого класса

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # вызываем метод __new__ базового класса и тем самым разрешаем создание объекта
        return cls.__instance  # Иначе, просто возвращаем ссылку на ранее созданный экземпляр


    def __init__(self, user, pws, port):
        self.user = user
        self.pws = pws
        self.port = port

    def connect(self):
        print(f'соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f'запись в БД {data}')

db = DataBase('root', '123', '80')
db2 = DataBase('root2', '5678', '40')
# ссылки db и db2 ведут на один объект
print(id(db), id(db2))  # 46087728 46087728
