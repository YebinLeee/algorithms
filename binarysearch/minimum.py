import sys

n = int(sys.stdin.readline())
a  = list(map(int, sys.stdin.readline().split()))
b  = list(map(int, sys.stdin.readline().split()))

a.sort()
print(sum(a[i]*b.pop(b.index(max(b))) for i in range(n))) # B 재배열 X