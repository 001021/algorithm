N = int(input())

array = list(map(int, input().split()))

v = int(input())

num = 0

for i in array:
  if (i == v):
    num = num + 1

print(num)
