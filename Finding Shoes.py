# cook your dish here
for _ in range(int(input())):
    a,b = map(int,input().split())
    if b == 0:
        print(a*2)
    elif a<=b:
        print(a)
    else:
        print((a*2)-b)
