# cook your dish here
for _ in range(int(input())):
    n = int(input())
    fper = n - (n/10)
    fdis = n-100
    if min(fper,fdis) == fper:
        print(int(n-fper))
    else:
        print(int(n-fdis))
    
