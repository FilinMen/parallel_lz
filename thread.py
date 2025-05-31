import threading
import time
import math
import multiprocessing 
import asyncio

class Factorial:

    def __init__(self, num):
        self.num = num

    def fac(self, n):
        return math.factorial(n)

    def seq(self): #последовательного
        start = time.time()
        results = [self.fac(n) for n in self.num]
        end = time.time()
        delta = end - start
        print(f"Время последовательного вычисления: {delta} секунд")

    def paral(self): #параллельного
        start = time.time()
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            results = pool.map(self.fac, self.num)
            pool.close()
            pool.join()
        end = time.time()
        delta = end - start
        print(f"Время параллельного вычисления: {delta} секунд")

progress = 0

def monitor():
    global progress
    progress += 1
    print(f"прогресс: {progress}/50")
    
def sleep():
    time.sleep(1)

async def error():
    await asyncio.sleep(3)
    raise ValueError("ОЙ")  

async def go():
    try:
        await error()
    except ValueError as e:
        print(f"Исключение обработано: {e}")


def main():
    print("ЗАДАНИЕ 1")
    for i in range(50):
        threads = threading.Thread(target=monitor, name="Thread-1")
        threads1 = threading.Thread(target=sleep, name="Thread-2")
        threads.start()
        threads1.start()
        threads.join()
        threads1.join()
    print("ЗАДАНИЕ 2")
    num = list(range(1, 501))
    calculator = Factorial(num)

    calculator.seq()
    calculator.paral()
    print("ЗАДАНИЕ 3")
    asyncio.run(go())

if __name__ == "__main__":
    main()