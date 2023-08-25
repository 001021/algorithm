N, k = map(int, input().split())

input = list(map(int, input().split()))

sort = sorted(input, reverse=True)

print(sort[k-1])