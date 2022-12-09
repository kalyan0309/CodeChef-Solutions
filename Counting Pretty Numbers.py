# cook your dish here
for i in range(int(input())):
    x,y = map(int, input().split(" "))
    count = 0
    for p in range(x,y+1):
        b = str(p)
        if b.endswith("2") or b.endswith("3") or b.endswith("9"):
            count += 1
        else:
            pass
    print(count)
