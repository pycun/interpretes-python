import time
from sum_of_squares import sum_of_squares
from sum_of_squares_cython import sum_of_squares_cython

numbers = list(range(1, 10000000))

# Medición del tiempo de ejecución para la versión de Python
start_time = time.time()
result_python = sum_of_squares(numbers)
end_time = time.time()
python_execution_time = end_time - start_time

# Medición del tiempo de ejecución para la versión de Cython
start_time = time.time()
result_cython = sum_of_squares_cython(numbers)
end_time = time.time()
cython_execution_time = end_time - start_time

print(f"Resultado (Python): {result_python}")
print(f"Tiempo de ejecución (Python): {python_execution_time:.4f} segundos")

print(f"Resultado (Cython): {result_cython}")
print(f"Tiempo de ejecución (Cython): {cython_execution_time:.4f} segundos")
