N = int(input()) 

movie_number = 665

movie_count = 0

while True:
  movie_number += 1
  if '666' in str(movie_number):
    movie_count += 1
  if movie_count == N:
    print(movie_number)
    break