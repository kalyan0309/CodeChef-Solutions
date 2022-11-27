# cook your dish here
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    e = a-c
    f = b-d 
    if e<=0:
        e = e*-1
    if f<=0:
        f = f*-1
    print(max(e,f))
