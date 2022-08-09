from multiprocessing import Pool
from time import time
from concurrent.futures import ProcessPoolExecutor


def factorize(*number):
    result = []
    for num in number:
        el_list = []
        div = num
        while num > 0:
            if div % num == 0:
                el_list.append(int(div / num))
            num -= 1
        result.append(el_list)
    return result


if __name__ == '__main__':
    timer = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
    print(f"Speed test Python default synchron work = {round(time() - timer, 4)} sec")

    timer_pool = time()
    with Pool(processes=4) as pool:
        pool.map(factorize, [128, 255, 99999, 10651060])
        print(f"Speed test with Pool (4 processes) = {round(time() - timer_pool, 4)} sec")

    timer_executor = time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(factorize, [128, 255, 99999, 10651060])
        print(f"Speed test with PoolExecutor (4 processes) = {round(time() - timer_executor, 4)} sec")












