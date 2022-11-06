# cook your dish here
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    lhs = (a**2)/(c**3)
    rhs = (b**2)/(d**3)
    if lhs == rhs:
        print("YES")
    else:
        print("NO")
