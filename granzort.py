#@@@bugfix
#powershell, CMD는 ANSI escape 인식 못 함
#사운드는 windows terminal에서만 정상 동작함..wav->mp3로 변경할 것

import time
import os
import winsound

winsound.PlaySound("granzort.wav", winsound.SND_ASYNC)

def distance(a,b):
    origin_x = row//2
    origin_y = col//2

    return ((origin_x - a)**2 + (origin_y - b)**2)

def draw_circle():
    for i in range(row+1):
        for j in range(col+1):
            dist = distance(i,j)
            if dist >= r**2-r/1.3 and dist <= r**2+r/1.3:
                array[i][j]="*"
            else:
                array[i][j]="  "
    for i in range(row+1):
        for j in range(col+1):
            time.sleep(0.005)
            print(array[i][j],end='')
            if(j==col):
                print("")

def draw_circle_back():
    for i in range(row+1):
        for j in range(col+1):
            dist = distance(i,j)
            if ((dist >= (r-2)**2-(r-2)/1.3) and (dist <= (r-2)**2+(r-2)/1.3)) or (dist >= r**2-r/1.3 and dist <= r**2+r/1.3):
                array[i][j]="*"
            else:
                array[i][j]="  "
    print('\033[F',end='\x1b[2K')
    for i in range(row+1):
        for j in range(col+1):
            time.sleep(0.01)
            print(array[i][j],end='')
            if(j==col):
                print("",end='\r')
                print('\033[F',end='\x1b[2K')

row=20
col=20   
array=[[0 for j in range(col+1)] for _ in range(row+1)]
center = array[row//2][col//2]
r = (row//2)

draw_circle()


# os.system('clear')
# row=10
# col=10
# array=[[0 for j in range(col)] for _ in range(row)]
# center = array[row//2][col//2]
# r = (row//2)
draw_circle_back()

for i in range(1):
    print("",end='\r')
    print('\033[F',end='\x1b[2K')