# cook your dish here
for _ in range(int(input())):
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    if c<a or d<b:
        print("IMPOSSIBLE")
    else:
        print('POSSIBLE')
