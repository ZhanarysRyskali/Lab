import math

def find_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def print_next_previous(n):
    print("The next number for the number", n, "is", n + 1, end=".\n")
    print("The previous number for the number", n, "is", n - 1, end=".")

def apples_per_student(n, k):
    return k // n

def apples_left_in_basket(n, k):
    return k % n

def vasya_position(v, t):
    return (v * t) % 109

    