import numpy as np

def step(a):
    one=np.ones(a.shape,dtype=np.int8)
    zero=np.zeros(a.shape,dtype=np.int8)
    maxX,maxY=a.shape
    maxX-=1
    maxY-=1
    a+=one
    flash=one.copy()
    while ((a>9)*flash).any():
        
        add=zero.copy()
        
        for x,row in enumerate((a>9)*flash):
            for y,cell in enumerate(row):
                if cell==1:
                    flash[x][y]=0
                    add[x][y]+=1
                    
                    if x!=0 and y!=0:add[x-1][y-1]+=1
                    if x!=maxX and y!=maxY:add[x+1][y+1]+=1
                    if x!=0 and y!=maxY:add[x-1][y+1]+=1
                    if x!=maxX and y!=0:add[x+1][y-1]+=1
                    if x!=0:add[x-1][y]+=1
                    if x!=maxX:add[x+1][y]+=1
                    if y!=0:add[x][y-1]+=1
                    if y!=maxX:add[x][y+1]+=1
        a+=add
    a*=flash
    return(a.size-flash.sum())


with open('11.txt') as inputVals:
    inp=inputVals.read().splitlines()

'''
inp="""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".splitlines()
'''

inp=np.array(list(map(lambda x: list(map(int,list(x))),inp)))
countFlash=0

for i in range(100):
    countFlash+=step(inp)
print(f'Part A: {countFlash}')

syncFlash=0
count=100
while syncFlash!=100:
    syncFlash=step(inp)
    count+=1
    
print(f'Part B: {count}')