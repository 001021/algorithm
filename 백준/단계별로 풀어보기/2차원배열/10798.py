array = []

for _ in range(5):
  array.append(list(input()))


for j in range(15):
  for i in range(5):
    if ( len(array[i]) <= j ): continue
    else: print(array[i][j], end='')
