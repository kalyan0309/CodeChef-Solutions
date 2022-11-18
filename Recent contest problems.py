# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = input().split()
    count=0
    count1=0
    for i in range(n):
        if a[i] == "START38":
            count+=1
        if a[i] == "LTIME108":
            count1+=1
    print(count,end=" ")
    print(count1)
            
            
        
