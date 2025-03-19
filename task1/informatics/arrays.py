def print_even_index_elements():
    n = int(input())
    arr = list(map(int, input().split()))
    print(*arr[::2])

def print_even_numbers():
    n = int(input())
    arr = list(map(int, input().split()))
    print(*[x for x in arr if x % 2 == 0])

def count_positive_numbers():
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(1 for x in arr if x > 0))

def count_greater_than_previous():
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(1 for i in range(1, n) if arr[i] > arr[i - 1]))

def has_same_sign_neighbors():
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(n - 1):
        if arr[i] * arr[i + 1] > 0:
            print("YES")
            return
    print("NO")

def count_local_peaks():
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = sum(1 for i in range(1, n - 1) if arr[i] > arr[i - 1] and arr[i] > arr[i + 1])
    
    print(count)

def reverse_in_place():
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    
    print(*arr)