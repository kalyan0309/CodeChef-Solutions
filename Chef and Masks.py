# cook your dish here
for _ in range(int(input())):
    a,b = map(int,input().split())
    c = a*100
    d = b*10
    if c == d:
        print("Cloth")
    elif c < d:
        print("Disposable")
    else:
        print("Cloth")
