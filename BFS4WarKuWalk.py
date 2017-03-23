'''
@Author - ReiiYuki
'''
import random

def randomMapCreate(size,obstacle) :
    list = []
    for i in range(0,size) :
        list.append([])
        for j in range(0,size) :
            list[i].append(0)

    for i in range(0,obstacle) :
        x = random.randint(0,size-1)
        y = random.randint(0,size-1)
        list[x][y] = 1
    return list

def printMap(map) :
    for i in map :
        for j in i :
            print (j,end = " ")
        print()

map = randomMapCreate(16,50)
printMap(map)
