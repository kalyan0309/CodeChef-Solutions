for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if abs(b-a) <=  c:
        print("YES")
    else:
        print("NO")
