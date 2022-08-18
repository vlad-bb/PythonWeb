# PythonWeb
This repository for learning Python Web

**Модуль 1**

Напишіть класи серіалізації контейнерів з даними Python у json, bin файли. Самі класи мають відповідати загальному інтерфейсу (абстрактному базовому класу) SerializationInterface.
Напишіть клас метаклас Meta, який усім класам, для кого він буде метакласом, встановлює порядковий номер. 

**Модуль 2**

Намалюйте UML діаграму вашого курсового застосунку "Персональний помічник". Для роботи можете скористатися безкоштовним draw.io або будь-яким іншим зручним для вас застосунком.
Ваш курсовий застосунок зараз працює в консольному режимі і взаємодіє з користувачем за допомогою команд в консолі. Застосунок потрібно розвивати і частиною застосунку, що найчастіше змінюється, зазвичай, є інтерфейс користувача (консоль поки що). Модифікуйте код вашого застосунку, щоб представлення інформації користувачеві (виведення карток з контактами користувача, нотатками, сторінка з інформацією про доступні команди) було легко змінити. Для цього треба описати абстрактний базовий клас для представлень користувача і конкретні реалізації, які наслідують базовий клас і реалізують консольний інтерфейс. Надалі ми розширюватимемо застосунок, додаючи туди Web-інтерфейс.

**Модуль 3**

Зараз ваш проект "Персональний помічник", швидше за все, існує як пакет у системі, встановлений глобально, і використовує версію Python, яка встановлена в системі зі встановленими в системі пакетами. Скористайтеся будь-яким зручним інструментом (pipenv, conda, poetry) для створення віртуального оточення для вашої програми. Зафіксуйте версію Python у цьому оточенні (вкажіть явно: який Python слід використовувати) та налаштуйте ваше робоче середовище (IDE) для роботи зі створеним оточенням.
Створіть Dockerfile, в якому встановіть "Персональний помічник" і запустіть його як окрему програму в окремому контейнері.

**Модуль 4**

Напишите программу обработки папки "Хлам", которая сортирует файлы в указанной папке по расширениям с использованием нескольких потоков. Ускорьте обработку больших каталогов с большим количеством вложенных папок и файлов, за счет параллельного выполнения обхода всех папок в отдельных потоках. Наиболее затратным по времени будет перенос файла и получение списка файлов в папке (итерация по содержимому каталога). Чтобы ускорить перенос файлов, его можно выполнять в отдельном потоке или пуле потоков. Это тем более удобно, что результат этой операции вы в приложении не обрабатываете и можно не собирать никакие результаты. Чтобы ускорить обход содержимого каталога с несколькими уровнями вложенности, вы можете обработку каждого подкаталога выполнять в отдельном потоке или передавать обработку в пул потоков.

**Модуль 5**

Напишите реализацию функции factorize, которая принимает список чисел и возвращает список чисел, на которые числа из входного списка делятся без остатка.
Реализуйте синхронную версию и измерьте время выполнения.
Потом улучшите производительность вашей функции, реализовав использование нескольких ядер процессора для параллельных вычислений, и замерьте время выполнения опять.
Для проверки правильности работы алгоритма самой функции можете воспользоваться тестом:
def factorize(*number):
    # YOUR CODE HERE
    raise NotImplementedError()

a, b, c, d  = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

**Модуль 5**

Напишите программу обработки папки "Хлам", которая сортирует файлы в указанной папке по расширениям с использованием asyncio. Чтобы перемещать и переименовывать файлы, воспользуйтесь асинхронной версией pathlib: [aiopath](https://pypi.org/project/aiopath).
