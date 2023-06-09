# cook your dish here
for _ in range(int(input())):
    n = list(map(int,input().split()))
    a = input()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    d={}
    s = 0
    for i in range(len(n)):
        d[alpha[i]] = n[i]
        
    for i in range(len(alpha)):
        if alpha[i] not in a:
            s+=d[alpha[i]]
        
    print(s)
