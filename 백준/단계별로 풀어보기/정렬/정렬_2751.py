import sys

def merge_sort(arr, start, end):

  if start < end:
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, mid, end)


def merge(arr, start, mid, end):
  sorted_arr = []
  left_idx = start
  right_idx = mid + 1

  while left_idx <= mid and right_idx <= end:
    if arr[left_idx] < arr[right_idx]:
      sorted_arr.append(arr[left_idx])
      left_idx += 1
    else:
      sorted_arr.append(arr[right_idx])
      right_idx += 1

  while left_idx <= mid:
    sorted_arr.append(arr[left_idx])
    left_idx += 1

  while right_idx <= end:
    sorted_arr.append(arr[right_idx])
    right_idx += 1

  for i in range(len(sorted_arr)):
    arr[start + i] = sorted_arr[i]

n = int(sys.stdin.readline())
arr = [ int(sys.stdin.readline()) for _ in range(n) ]
merge_sort(arr, 0, n-1)

for num in arr:
  print(num)
  