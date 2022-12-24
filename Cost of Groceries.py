# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))[:n]
    b=list(map(int,input().split()))[:n]
    t = 0
    for i in range(n):
        if a[i]>=x:
            t+=b[i]
    print(t)
    
