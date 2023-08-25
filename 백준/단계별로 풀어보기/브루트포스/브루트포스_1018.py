N, M = map(int, input().split())

board = []

for n in range(N):
  board.append(list(input()))

# 올바른 체스 보드판 - 검은색으로 시작하는 보드판
black_start_board = [
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB"
]

# 올바른 체스 보드판 - 흰색으로 시작하는 보드판
white_start_board = [
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW"
]

# 정답
result = 1e9

# 8*8 체스판 만들기
for i in range(N - 7):
  for j in range(M - 7):

    # 만들어진 8*8 체스판
    temp_chess = [lst[j : j + 8] for lst in board[i : i + 8]]

    # 검은색 보드에 대해 다른 수 카운팅
    black_count = 0

    # 흰색 보드에 대해 다른 수 카운팅
    white_count = 0

    # 각 가짓수에 대해 검사
    for k in range(8):
      for l in range(8):
        if temp_chess[k][l] != black_start_board[k][l]:
          black_count += 1

        if temp_chess[k][l] != white_start_board[k][l]:
          white_count += 1

    temp_result = 0
    
    if (black_count > white_count):
      temp_result = white_count
    else:
      temp_result = black_count

    if (temp_result < result):
      result = temp_result

print(result)
    
