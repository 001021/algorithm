N = int(input())

result = []

for _ in range(N):
  result.append(int(input()))

result_sort = sorted(result)

for data in result_sort:
  print(data)

