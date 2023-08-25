bucket = []

for i in range(31):
  bucket.append(0)

for i in range(28):
  bucket[int(input())] = 1

for i in range(1, 31):
  if (bucket[i] == 0):
    print(i)
