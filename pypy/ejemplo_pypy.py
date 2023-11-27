# PyPy
import time

def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total


numbers = list(range(1, 10000000))
start_time = time.time()
resultado_pypy = sum_of_squares(numbers)
end_time = time.time()
print("Resultado PyPy:", resultado_pypy)
print("Tiempo de ejecución en PyPy:", end_time - start_time, "segundos")