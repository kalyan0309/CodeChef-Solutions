# cook your dish here
for _ in range(int(input())):
    a = int(input())
    d = a//3
    if a%3 == 0:
        print("0")
    else:
        print(((d+1)*3)-a)
