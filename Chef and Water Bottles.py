# cook your dish here
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if c//b < a:
        print(c//b)
    elif c//b > a:
        print(a)
    else:
        print("0")
