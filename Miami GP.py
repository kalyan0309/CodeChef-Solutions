# cook your dish here
for _ in range(int(input())):
    X,Y=map(int,input().split())
    a=X*(107/100)
    if a>=Y:
        print("YES")
    else:
        print("NO")
