# cook your dish here
for _ in range(int(input())):
    n,s,r,sa = map(int,input().split())
    if n>=s:
        s = r+s
    elif s>n:
        n = r+n
    if min(s,n) == s:
        s = sa+s
    else:
        n = sa+n
    if min(s,n) == s:
        print("N")
    else:
        print("S")
            
        
        
