import sda as s

def main():
    numbers = list(range(1, 501))  # Числа от 1 до 500
    
    # Параллельное вычисление
    parallel_results, parallel_time = parallel_factorials(numbers)
    
    # Последовательное вычисление
    sequential_results, sequential_time = sequential_factorials(numbers)
