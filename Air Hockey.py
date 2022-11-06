# cook your dish here
for _ in range(int(input())):
    a,b = map(int,input().split())
    r = min(a,b)
    if r == a and r==b:
        print(7-r)
    elif r == a:
        print(7-b)
    else:
        print(7-a)
