# cook your dish here
for _ in range(int(input())):
    a = int(input())
    if a<4:
        print("MILD")
    elif a>=4 and a<7:
        print("MEDIUM")
    else:
        print("HOT")
