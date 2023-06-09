# cook your dish here
for _ in range(int(input())):
    n = int(input())
    pm = list(map(int,input().split()))
    count=0
    for i in range(0,n):
        if i==0:
            if pm[i] != pm[i+1]:
                count+=1
        elif i==n-1:
            if pm[i] != pm[i-1]:
                count+=1 
        elif pm[i] != pm[i-1] or pm[i] != pm[i+1]:
                count+=1 
        else:
            count+=0
    print(count)
                
