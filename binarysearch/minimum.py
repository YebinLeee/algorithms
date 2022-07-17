import sys

n = int(sys.stdin.readline())
a  = list(map(int, sys.stdin.readline().split()))
b  = list(map(int, sys.stdin.readline().split()))

a.sort()
ans = 0
for i in range(n):
  ans += a[i] * b.pop(b.index(max(b))) # B 재배열 X

print(ans)