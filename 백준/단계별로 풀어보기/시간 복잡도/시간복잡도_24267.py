from math import comb

n = int(input())

# 코드1의 수행 횟수 계산
perform_count = comb(n, 3)

# 최고차항 차수 계산
highest_degree = 3

print(perform_count)
print(highest_degree)