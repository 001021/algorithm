def palindrome(str):
  j = len(str) - 1
  for i in range(len(str)):
    if (str[i] != str[j]):
      return 0
    j -= 1
    if (i >= j): break
  return 1
    
    
input = input()

print(palindrome(input))

