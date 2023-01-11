# cook your dish here
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a==b or b==c or a==c:
        print("NO")
    else:
        print("YES")
