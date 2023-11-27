# sum_of_squares_cython.pyx
def sum_of_squares_cython(numbers):
    total = 0
    for num in numbers:
        total += num * num
    return total
