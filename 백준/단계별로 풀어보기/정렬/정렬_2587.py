input = [ int(input()) for _ in range(5) ]

sort = sorted(input)

print(sum(sort) // 5)
print(sort[2])