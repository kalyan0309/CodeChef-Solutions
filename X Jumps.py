# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    c=x%y
    p=x//y
    if x%y==0:
        print(x//y)
    elif x<y:
        print(x)
    elif x%y!=0 and x>y:
        print(p+c)
