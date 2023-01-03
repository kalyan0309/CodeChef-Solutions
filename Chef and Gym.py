# cook your dish here
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a+b <= c:
        print("2")
    elif a+b > c:
        if a<=c:
            print("1")
        else:
            print("0")
    else:
        print("0")
        
