n = int(input())

strnum = list(map(int, str(n)))

sort = sorted(strnum, reverse = True)

for num in sort:
  print(num, end='')
