# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = [6,13,20,27,7,14,21,28]
    count = 0
    for i in a:
        if i not in s:
                count+=1
    print(count+len(s))
