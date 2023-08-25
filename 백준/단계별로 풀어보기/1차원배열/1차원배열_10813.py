N, M = map(int, input().split())

bucket = [0]

for n in range(N):
  bucket.append(n)

for m in range(M):
  i, j = map(int, input().split())

  temp = bucket[i]
  bucket[i] = bucket[j]
  bucket[j] = temp

for data in bucket:
  print(data, end=' ')
