# cook your dish here
for _ in range(int(input())):
    a,b = map(int,input().split())
    num = a+b
    num1 = 21-num
    if num1 in range(1,11):
        print(num1)
    else:
        print("-1")
        
