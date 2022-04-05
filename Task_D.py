l = list(map(int, input().split()))
n = l[0]
k = l[1]
a_int = sorted(a_int)
a_sum = sum(a_int)
a_max = max(a_int)
a_str = list(map(lambda x: str(x).zfill(len(str(a_max))), a_int))
sums = 0
ind = 0
while True:
  if ind == len(str(a_max)): break
  a_str.sort(key=lambda x: x[ind])
  for an, ai in enumerate(a_str):
    if k == 0: break
    lai = list(ai)
    if lai[ind] != '0' and lai[ind] !='9':
      lai[ind] = '9'
      a_str[an] = ''.join(lai)
      k -= 1
  else:
    ind += 1
    continue
  break
print(sum(list(map(int, a_str))) - a_sum)
