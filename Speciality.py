# cook your dish here
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    r = max(a,b,c)
    if r == a:
        print("Setter")
    elif r == b:
        print("Tester")
    else:
        print("Editorialist")
