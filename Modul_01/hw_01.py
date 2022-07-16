""" Домашнее задание
1) Напишите классы сериализации контейнеров с данными Python в json, bin файлы.
Сами классы должны соответствовать общему интерфейсу (абстрактному базовому классу) SerializationInterface.
2) Напишите класс метакласс Meta, который всем классам, для кого он будет метаклассом, устанавливает порядковый номер.
Код для проверки правильности решения:
class Meta(type):
    # тут должно быть ваше решение


Meta.children_number = 0

class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1) """

# Задача 1
from abc import ABCMeta, abstractmethod
import json
import pickle
from my_logger import get_logger

logger = get_logger(__name__)


class SerializationInterface(metaclass=ABCMeta):
    def __init__(self, data, filename):
        self.data = data
        self.__filename = None
        self.filename = filename
        logger.info(f'{self.filename}')

    @abstractmethod
    def serialize(self):
        pass

    @abstractmethod
    def deserialize(self):
        pass


class SerializeJson(SerializationInterface):
    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename):
        parse = filename.split('.')
        if parse[1] == 'json':
            self.__filename = filename
        else:
            logger.warning(f'{ValueError}')
            raise ValueError("File must be JSON format")

    def serialize(self):
        with open(self.__filename, 'w') as file:
            json.dump(self.data, file, ensure_ascii=False)
            logger.info(f'{self.data}')

    def deserialize(self):
        with open(self.__filename, 'r') as file:
            unpacked = json.load(file)
            print(unpacked)
            logger.debug(f'{unpacked}')


class SerializeBin(SerializationInterface):
    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename):
        parse = filename.split('.')
        if parse[1] == 'bin':
            self.__filename = filename
        else:
            raise ValueError("File must be BIN format")

    def serialize(self):
        with open(self.__filename, 'wb') as file:
            pickle.dump(self.data, file)

    def deserialize(self):
        with open(self.__filename, 'rb') as file:
            unpacked = pickle.load(file)
            print(unpacked)


# задание 2

class Meta(type):
    class_number = 0
    children_number = 0
    logger.debug(f'{children_number, class_number}')

    def __new__(cls, *args):
        instance = type.__new__(cls, *args)
        if cls.children_number == 0:
            cls.class_number = 0
        instance.class_number = cls.class_number
        cls.class_number += 1
        cls.children_number += 1
        logger.info(f'{instance}')
        return instance


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


if __name__ == '__main__':
    assert (Cls1.class_number, Cls2.class_number) == (0, 1)
    a, b = Cls1(''), Cls2('')
    assert (a.class_number, b.class_number) == (0, 1)
    test_data = {'name': 'Vladyslav', 'phone': ['0936007646', '0637362574'], 'age': 32}

    json_test = SerializeJson(test_data, 'DB.json')
    json_test.serialize()
    json_test.deserialize()
    # json_test_wrong = SerializeJson(test_data, 'DB.txt')

    bin_test = SerializeBin(test_data, 'DB.bin')
    bin_test.serialize()
    bin_test.deserialize()
