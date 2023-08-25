grade = []

# 20 X 3 matrix
for _ in range(20):
  grade.append(list(input().split()))

sum = 0
gradeSum = 0

for i in range(len(grade)):
  if (grade[i][2] == 'A+'): gradeNum = 4.5
  elif (grade[i][2] == 'A0'): gradeNum = 4.0
  elif (grade[i][2] == 'B+'): gradeNum = 3.5
  elif (grade[i][2] == 'B0'): gradeNum = 3.0
  elif (grade[i][2] == 'C+'): gradeNum = 2.5
  elif (grade[i][2] == 'C0'): gradeNum = 2.0
  elif (grade[i][2] == 'D+'): gradeNum = 1.5
  elif (grade[i][2] == 'D0'): gradeNum = 1.0
  elif (grade[i][2] == 'F'): gradeNum = 0.0
  elif (grade[i][2] == 'P'): continue

  gradeSum += float(grade[i][1])
    
  sum += gradeNum * float(grade[i][1])

print('%6f'%(sum/gradeSum))


