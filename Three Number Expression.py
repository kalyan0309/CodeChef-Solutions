# cook your dish here
for _ in range(int(input())):
    a =sorted(list(map(int,input().split())))
    if a[2] - (a[0]+a[1]) == 0:
        print("YES")
    else:
        print("NO")
    
