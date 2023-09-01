def counting_sort(arr):
  # 입력 배열 전체를 스캔해서 최대값 K를 찾는다.
  max_arr = max(arr)

  # 카운팅 배열을 생성한다.
  count = [0] * (max_arr + 1)
  sorted_arr = list()

  # 입력 배열의 값을 기준으로 원소 개수를 업데이트한다.
  for i in arr:
    count[i] += 1

  # 카운팅 배열을 정렬 배열로 바꿔준다.
  for i in range(max_arr + 1):
    for _ in range(count[i]):
      sorted_arr.append(i)
