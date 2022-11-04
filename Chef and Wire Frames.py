# cook your dish here
for _ in range(int(input())):
    l,w,r = map(int,input().split())
    per = 2*(l+w)
    print(per*r)
