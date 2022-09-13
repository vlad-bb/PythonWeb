import timeit
import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)
"""
Программа приймає на вхід число та його ступінь, і методом рекурсії знаходить результат.
Було розробленно 2 варіанти:
1. Функція convert() - яка рекурсивно рахує результат.
2. Функція convert_cache_redis() - яка також рекурсивно рахує результат,
 але має кеш - реальзований за допомогою Redis LRU.
 Для запуску прикладу необхідно запустити Docker контейнер з Redis! Для запуску введіть в термінал наступний код:
 docker run --name redis_rec -p 6379:6379 -d redis
 
"""


def convert(base, exp):
    if exp == 1:
        return base
    if exp != 1:
        return base * convert(base, exp - 1)


@cache
def convert_cache_redis(base, exp):
    if exp == 1:
        return base
    if exp != 1:
        return base * convert(base, exp - 1)


if __name__ == '__main__':
    base_num = int(input("Введіть число: "))
    exp_num = int(input("Введіть його ступень: "))
    start_time = timeit.default_timer()
    result = convert(base_num, exp_num)
    print(f'Result {result}\nDuration without cache: {timeit.default_timer() - start_time} sec')

    print('-' * 50)

    start_time = timeit.default_timer()
    result_cache = convert_cache_redis(base_num, exp_num)
    print(f'Result {result_cache}\nDuration with Redis cache: {timeit.default_timer() - start_time}')
