N, M = map(int, input().split())

bucket = [0]

for n in range(N):
  bucket.append(0)

for m in range(M):
  i, j, k = map(int, input().split())

  for p in range(i, j + 1):
    bucket[p] = k

for data in bucket[1:]:
  print(data, end=' ')
