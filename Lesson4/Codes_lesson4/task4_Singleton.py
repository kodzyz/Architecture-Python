# pythonpip.ru
class GovtSingleton:
    __instance = None

    def __init__(self):

        if GovtSingleton.__instance is None:
            GovtSingleton.__instance = self
        else:
            raise Exception('We can not creat another class')

    @classmethod
    def get_instance(cls):  # возвращает существующий экземпляр
        if not cls.__instance:
            GovtSingleton()  # при создании __instance := экземпляр(в конструкторе__init__)
            # return cls.__instance
        return cls.__instance

db = GovtSingleton()
print('db=', db) # <__main__.GovtSingleton object at 0x024A3970>
db2 = GovtSingleton.get_instance()
print('db2=', db2) # <__main__.GovtSingleton object at 0x024A3970>

db3 = GovtSingleton.get_instance()
print('db3=', db3) # <__main__.GovtSingleton object at 0x024A3970>
print(id(db), id(db2), id(db3))  # 38418800 38418800 38418800

db4 = GovtSingleton() # один экземпляр уже есть db
print('db4=', db4) # We can not creat another class
