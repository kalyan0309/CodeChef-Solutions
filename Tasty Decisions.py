# cook your dish here
for _ in range(int(input())):
    a,b = map(int,input().split())
    c = 2*a 
    d = 5*b 
    if c>d:
        print("Chocolate")
    elif c == d:
        print("Either")
    else:
        print("Candy")
