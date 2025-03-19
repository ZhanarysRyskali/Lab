def perfect_squares(n):
    i = 1
    while i * i <= n:
        print(i * i)
        i += 1

def smallest_divisor(n):
    i = 2
    while n % i != 0:
        i += 1
    return i

def powers_of_two(n):
    power = 1
    while power <= n:
        print(power, end=" ")
        power *= 2

def is_power_of_two(n):
    while n > 1:
        if n % 2 != 0:
            print("NO")
            return
        n //= 2
    print("YES")

def smallest_power_of_two(n):
    k = 0
    power = 1
    while power < n:
        power *= 2
        k += 1
    print(k)

