from abc import ABCMeta, abstractmethod


class Subject:
    '''за ним следим'''

    def __init__(self):
        self._observers = set()  # set() = {} подписчики(наблюдатели)
        self._subject_state = None  # состояние

    def attach(self, observer):
        '''добавить наблюдателя в список подписчиков'''
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        '''убрать наблюдателя'''
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        '''обойти подписчиков сказать о смене состояния'''
        for observer in self._observers:
            observer.update(self._subject_state)


class Observer(metaclass=ABCMeta):
    '''абстрактный наблюдатель'''

    def __init__(self):
        self._subject = None  #
        self._observer_state = None

    @abstractmethod
    def update(self, arg):
        pass


class Sensor(Subject):
    '''
    за ним следим - градусник
    изменяется температура - получаем сообщения'''

    @property
    def t(self):
        return self._subject_state

    @t.setter
    def t(self, t):
        self._subject_state = t
        self._notify()  # при изменении - оповещение об изменении температуры


class SmsNotifier(Observer):
    '''Sms наблюдатель'''

    def update(self, arg):
        if arg > 50:
            print('send sms', 'куда так горячо!')


class DisplayObserver(Observer):
    '''Display наблюдатель'''
    def update(self, arg):
        print(f'{self.__class__.__name__} temperature {arg}')


class HeaterObserver(Observer):
    def __init__(self, low_threshold, step):
        super().__init__()
        self.low_threshold = low_threshold
        self.step = step

    def update(self, arg):
        if isinstance(self._subject, Sensor):
            sensor = self._subject

            t = sensor.t
            delta_low = t - self.low_threshold

            if delta_low < 0:
                t += self.step
                print(f'{self.__class__.__name__} heat impulse +{self.step}')
                sensor.t = t


# сенсором
sensor = Sensor()  # следим за ним - сенсор

# подключаем к сенсору наблюдателей за ним
sensor.attach(DisplayObserver())
sensor.attach(HeaterObserver(40, 20))
sensor.attach(SmsNotifier())

# изменяем состояние сенсора: сработает setter а в нем _notify оповещение
sensor.t = 20
