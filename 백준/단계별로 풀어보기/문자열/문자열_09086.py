T = int(input())

result = []

for t in range(T):
  str = ""
  S = input()

  str += S[0]
  str += S[len(S) - 1]

  result.append(str)

for t in range(T):
  print(result[t])
