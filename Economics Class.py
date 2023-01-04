# cook your dish here
for _ in range(int(input())):
    a = int(input()) 
    arr = list(map(int,input().split()))
    arr1 = list(map(int,input().split()))
    count=0
    for i in range(a):
        if arr[i] == arr1[i]:
            count+=1 
    print(count)
    
