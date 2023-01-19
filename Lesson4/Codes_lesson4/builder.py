'''Строитель'''
# Цель – у нас есть сложный объект.
# Который мы хотим строить по частям
# и не зависеть от представлений.

from abc import ABCMeta, abstractmethod


class TableDirector:
    '''
    Класс директор
    последовательность шагов процесса
    '''

    def __init__(self):
        self._builder = None  # В него будет передаваться объект строителя

    def construct(self, builder):
        '''
        Класс директор говорит следующее:
         сначала строй ножки потом столешницу
         '''
        self._builder = builder
        self._builder._build_legs()
        self._builder._build_tabletop()
        self._builder._build_coverage()


class Table:
    tabletop = 0
    legs = 0
    coverage = ''


class AbstractTableBuilder(metaclass=ABCMeta):
    '''абстрактный строитель с тремя методами'''

    def __init__(self):
        self.product = Table()

    @abstractmethod
    def _build_tabletop(self):
        pass

    @abstractmethod
    def _build_legs(self):
        pass

    @abstractmethod
    def _build_coverage(self):
        pass


class BigTableBuilder(AbstractTableBuilder):
    '''строитель1 со своими особенностями'''

    def _build_tabletop(self):
        self.product.tabletop = 120

    def _build_legs(self):
        self.product.legs = 4

    def _build_coverage(self):
        self.product.coverage = 'vanish'


class SmallTableBuilder(AbstractTableBuilder):
    '''строитель2 со своими особенностями'''

    def _build_tabletop(self):
        self.product.tabletop = 80

    def _build_legs(self):
        self.product.legs = 3

    def _build_coverage(self):
        self.product.coverage = 'yacht lacquer'


# создаем объекты строителей
big_table__builder = BigTableBuilder()
small_table__builder = SmallTableBuilder()

# запуск процесса конструирования
# объект директора
director = TableDirector()
# и передаем ему разных строителей
director.construct(big_table__builder)
director.construct(small_table__builder)
# Т.е. каждый строитель построит по-своему,
# но порядок стройки четко определит директор.

# берем сконструированное изделие
big_table_1 = big_table__builder.product  # это экзэмпляр класс Стол от строителя big
small_table_1 = small_table__builder.product  # это экзэмпляр класс Стол от строителя small

print(big_table_1.coverage)  # vanish
print(small_table_1.coverage)  # yacht lacquer

print(big_table_1.legs)  # 4
print(small_table_1.legs)  # 5
