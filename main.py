# имитация многопоточной работы с файлами

import threading
import time

def write_file(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    time.sleep(1)
    f.close()

# обычная запись
start = time.time()
for i in range(10):
    write_file(f"simple_file0{i}.txt","Hello! I'm file № {i}")
delta = time.time() - start
print(f"simple time of writing {i+1} files is: {delta}")

# Многопоточная запись
start = time.time()
thread1 = []
for i in range(10):
    threads = threading.Thread(target=write_file, args=(f"simple_file1{i}.txt","Hello! I'm file № {i}"))
    threads.start()
    thread1.append(threads)
    print(thread1)

for t in threads:
    t.join()

delta = time.time() - start
print(f"simple time of writing {i+1} files is: {delta}")
