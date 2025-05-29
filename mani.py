import multiprocessing
import time

def calculator(data):
    return sum(x**2 for x in data)


data = list()
# обычная запись
start = time.time()
result = calculator(data)
delta = time.time() - start
print(f"simple time of calculating is: {delta}")

# num = 2 #колличество процессов 
# Многопроцессорность запись
start = time.time()
pool = multiprocessing.Pool(processes=4)
parts = [data[i::4] for i in range(4)]
results = pool.map(calculator, parts)
pool.close()
pool.join()
result = sum(results)
delta = time.time() - start
print(f"simple time of calculating is  is: {delta} with {4} processes")
