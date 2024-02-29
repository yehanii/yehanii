from random import *
range=100
i=1
while range>0:
    dice=randint(1,6)
    range-=dice
    print("주사위 : ",dice)
    print(f"{i}번 진행 남은거리 {range}")
    print(i,range,sep="번 진행 남은거리 : ")
    i+=1