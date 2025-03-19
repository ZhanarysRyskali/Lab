#1
print("Hello, World!")

#2
n = int(input().strip())
if((n % 2 == 0 and 2 <= n <= 5) or (n % 2 == 0 and n > 20)):
    print("Not Weird")
else:
    print("Weird")

#3
a = int(input())
b = int(input())

print(a+b)
print(a-b)
print(a*b)

#4
a = int(input())
b = int(input())
print(a//b)
print(float(a/b))

#5
n = int(input())
for i in range(1, n+1):
    print(i, end = "")

#6
n = int(input())
for i in range(n):
    print(i*i)

#7
def is_leap(year):
    leap = False
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    
    return leap

year = int(input())
print(is_leap(year))

#8
students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set([score for _, score in students]))


second_lowest = scores[1]


result = sorted([name for name, score in students if score == second_lowest])

for name in result:
    print(name)

#9
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))

#10
n = int(input())
arr = map(int, input().split())
arr1 = set(arr)
arr2 = sorted(arr1)
print(arr2[-2])