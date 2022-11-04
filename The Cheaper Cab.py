# cook your dish here
for _ in range(int(input())):
    n,m = map(int,input().split())
    if n==m:
        print("ANY")
    elif min(n,m) == n:
        print("FIRST")
    else:
        print("SECOND")
