n, m = map(int, input().split())

A = []
B = []
C = []

for _ in range(n):
  A.append(list(map(int, input().split())))

for _ in range(n):
  B.append(list(map(int, input().split())))


for i in range(n):
  row = []
  for j in range(m):
    # if (A[i][j] < 0 and B[i][j] < 0): row.append(A[i][j])
    row.append(A[i][j] + B[i][j])
  C.append(row)

for row in C:
  print(*row)