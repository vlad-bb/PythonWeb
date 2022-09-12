import timeit
from functools import lru_cache
import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@cache
def fibonacci_cache_redis(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_cache_redis(n - 1) + fibonacci_cache_redis(n - 2)


@lru_cache
def fibonacci_cache_ft(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_cache_ft(n - 1) + fibonacci_cache_ft(n - 2)


start_time = timeit.default_timer()
fibonacci(8)
print(f'Duration without cache: {timeit.default_timer() - start_time}') #Duration: 2.1169005776755512e-05

start_time = timeit.default_timer()
fibonacci_cache_redis(200)
print(f'Duration with Redis cache: {timeit.default_timer() - start_time}') #Duration: 0.01373043299827259

start_time = timeit.default_timer()
fibonacci_cache_ft(200)
print(f'Duration with functool cache: {timeit.default_timer() - start_time}') #Duration: 0.000553067002329044


