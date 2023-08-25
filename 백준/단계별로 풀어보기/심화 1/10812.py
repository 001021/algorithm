N, M = map(int, input().split())

bucket = [i + 1 for i in range(N)]

for _ in range(M):
  begin, end, mid = map(int, input().split())

  bucket[begin-1:end] = bucket[mid-1:end] + bucket[begin-1:mid-1]

print(*bucket)