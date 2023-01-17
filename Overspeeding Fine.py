# cook your dish here
for _ in range(int(input())):
    fine = 0
    speed = int(input())
    if speed <= 70:
        fine+=0 
    elif speed >70 and speed <=100:
        fine+=500
    else:
        fine+=2000
    print(fine)
    
