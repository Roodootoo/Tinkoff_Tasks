#решение частичное...
l = list(map(int, input().split()))
n_dog = l[0]
time = l[1]
levels = list(map(int, input().split()))
level_time = int(input()) 
max_l = max(levels)
min_l = min(levels)
if (level_time > time):
  print(min(max_l - min_l + max_l - level_time, max_l - min_l + level_time - min_l))
else:
  print(max_l - min_l)
