'''
@Author - ReiiYuki
'''
import random
import queue

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

def BFS(map,x,y,targetX,targetY) :
    history = dict()
    s = []
    q = queue.Queue()
    s.append((x,y))
    q.put((x,y))
    reach = False
    while q.qsize() > 0 or not reach:
        current = q.get()
        x = current[0]
        y = current[1]
        if current[0] == targetX and current[1] == targetY :
            reach = True
            s.append((x,y))
        else :
            if (x+1,y) not in s and x+1<len(map) and map[x+1][y] != 1 :
                s.append((x+1,y))
                q.put((x+1,y))
                history[(x+1,y)] = current
            if (x-1,y) not in s and x-1>=0 and map[x-1][y] != 1:
                s.append((x-1,y))
                q.put((x-1,y))
                history[(x-1,y)] = current
            if (x,y+1) not in s and y+1<len(map) and map[x][y+1] != 1:
                s.append((x,y+1))
                q.put((x,y+1))
                history[(x,y+1)] = current
            if (x,y-1) not in s and y-1>=0 and map[x][y-1] != 1:
                s.append((x,y-1))
                q.put((x,y-1))
                history[(x,y-1)] = current
    path = []
    path.append((targetX,targetY))
    current = (targetX,targetY)
    while current in history :
        current = history[current]
        path.append(current)
    return path[::-1]

def showWalk(map,path) :
    for i in path :
        map[i[0]][i[1]] = '*'
        printMap(map)
        print ()
map = randomMapCreate(16,50)
printMap(map)
path = BFS(map,0,8,15,15)
showWalk(map,path)
