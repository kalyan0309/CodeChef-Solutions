# cook your dish here
for _ in range(int(input())):
    a,b = map(int,input().split())
    if (b//3)>=a:
        print("YES")
    else:
        print("NO")
