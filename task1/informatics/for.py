import math

def print_even_numbers(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=" ")

def print_numbers_with_remainder(a, b, c, d):
    for i in range(a, b + 1):
        if i % d == c:
            print(i, end=" ")

def print_perfect_squares(a, b):
    for i in range(math.ceil(math.sqrt(a)), math.floor(math.sqrt(b)) + 1):
        print(i * i, end=" ")

def count_digit_occurrences(x, d):
    return str(x).count(str(d))

def sum_of_digits(x):
    return sum(int(digit) for digit in str(x))

def reverse_number(x):
    return int(str(x)[::-1])

def smallest_divisor(x):
    for i in range(2, x + 1):
        if x % i == 0:
            return i

def print_divisors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i, end=" ")

def count_divisors(x):
    count = 0
    sqrt_x = int(math.sqrt(x))
    for i in range(1, sqrt_x + 1):
        if x % i == 0:
            count += 1 if i == x // i else 2
    return count

def sum_100_numbers():
    return sum(int(input()) for _ in range(100))

def sum_n_numbers():
    n = int(input())
    return sum(int(input()) for _ in range(n))

def binary_to_decimal():
    binary = input()
    decimal = 0
    length = len(binary)
    
    for i in range(length):
        decimal += int(binary[i]) * (2 ** (length - 1 - i))
    
    return decimal

def count_zeros():
    n = int(input())
    return sum(1 for _ in range(n) if int(input()) == 0)
