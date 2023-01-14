# cook your dish here
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if (a+b)/2 < 35 or (a+c)/2 < 35 or (b+c)/2 < 35:
        print("Fail")
    else:
        print("Pass")
        
        
        
