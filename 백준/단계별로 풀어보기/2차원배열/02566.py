array = []

for i in range(9):
  array.append(list(map(int, input().split())))

max = array[0][0]
column = -1
row = -1

for i in range(9):
  for j in range(9):
    if (array[i][j] >= max):
      max = array[i][j]
      column = i
      row = j

print(max)
print(column + 1, row + 1)