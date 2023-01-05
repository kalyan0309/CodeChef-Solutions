# cook your dish here
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a in range(b,c+1):
        print("Take second dose now")
    elif a <b:
        print("Too Early")
    else:
        print("Too Late")
        
