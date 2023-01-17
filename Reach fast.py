# cook your dish here
for _ in range(int(input())):
    (x, y, k) = map(int, input().split(' '))
    diff = abs(y - x)
    move = diff // k 
    if diff%k > 0:
        move += 1 
    print(move)
