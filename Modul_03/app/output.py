import json
from abc import ABC, abstractmethod


class AbstractOutput(ABC):
    """ Абстрактний базовий класс, для різних типів виводу(в консоль, web) """

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def output(self):
        pass


class CLIOutput(AbstractOutput):
    """ Класс виводу в консоль """

    def output(self):
        return self.data


class WebOutput(AbstractOutput):
    """ Класс виводу в web """
    file_name = 'request.json'

    def output(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.data, file, ensure_ascii=False)
            return self.file_name

    def send(self):
        """ Функція відправки даних до Web """
        pass


class Connection:
    """ Класс підключення до web """
    def __init__(self):
        pass


connection = Connection()


def separator(func):
    """ Декоратор для статичних функцій, в залежності від підключення до Web виводять інформацію в консоль чи в Web """
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        data.__str__()
        if data:
            if connection:
                result = WebOutput(data).output().send()
                return result
            elif not connection:
                result = CLIOutput(data)
                result.output()
                return result
        return wrapper
