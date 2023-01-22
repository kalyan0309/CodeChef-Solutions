# cook your dish here
for _ in range(int(input())):
    length = int(input())
    playlist = list(map(int,input().split()))
    pos = int(input())
    value = playlist[pos-1]
    playlist.sort()
    for i in range(0,length):
        if playlist[i] == value:
            print(i+1)
            
