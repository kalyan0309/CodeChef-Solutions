# cook your dish here
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    tot = 2*(180+a)
    tot_end = b+c
    print(tot-tot_end)
