N, M = map(int, input().split())

bucket = [0]

for n in range(1, N + 1):
  bucket.append(n)

for m in range(M):
  i, j = map(int, input().split())

  while (i <= j):
    temp = bucket[i]
    bucket[i] = bucket[j]
    bucket[j] = temp
    i = i + 1
    j = j - 1

for data in bucket[1:]:
  print(data, end=' ')
