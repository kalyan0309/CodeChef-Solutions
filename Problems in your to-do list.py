# cook your dish here
for _ in range(int(input())):
    n  = int(input())
    arr = list(map(int,input().split()))
    count=0
    for i in range(n):
        if arr[i]>=1000:
            count+=1
    print(count)
        
