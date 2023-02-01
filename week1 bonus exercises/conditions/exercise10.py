a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c-a == 0 or d-b == 0:
    print("YES")
elif (c-a)/(d-b) == 1:
    print("YES")
elif a+b == c+d:
    print("YES")
else:
    print("NO")