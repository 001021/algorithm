N = int(input())

n = N - 1

for i in range(1, 2*N, 2):
  print(' ' * n, end='')
  print('*' * i)
  n -= 1

n = 1

for i in range(2*N-3, 0, -2):
  print(' ' * n, end='')
  print('*' * i)
  n += 1