# cook your dish here
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    d1 = a+b
    d2 = c+d
    if min(d1,d2) == d1:
        print(d1)
    else:
        print(d2)
