n = int(input())
m = int(input())
x = int(input())
y = int(input())

k = 999
if (n < m):
    m, n = n, m
if (x < y):
    k = x
else:
    k = y
if (m == x or n == y):
    k = 0
if (m - x < k):
    k = m - x
if (n - y < k):
    k = n - y
print(k)
