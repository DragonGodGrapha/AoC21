from scipy import ndimage
from numpy import array, count_nonzero
with open('09.txt') as inputVals:
    inp=inputVals.read().splitlines()
    
"""
inp='''2199943210
3987894921
9856789892
8767896789
9899965678'''.splitlines()
"""

inp=list(map(list,inp))
for i,j in enumerate(inp):
    inp[i]=list(map(int,j))

lows=[]
for yp,row in enumerate(inp):
    for xp,cell in enumerate(row):
        
        if yp!=0:
            if inp[yp-1][xp]<=cell:
                continue
        if yp!=len(inp)-1:
            if inp[yp+1][xp]<=cell:
                continue
        if xp!=0:
            if inp[yp][xp-1]<=cell:
                continue
        if xp!=len(row)-1:
            if inp[yp][xp+1]<=cell:
                continue
        lows.append(cell+1)
print(f'Part A: {sum(lows)}')

inputArray=array(inp)
image=ndimage.label(inputArray<9)[0].ravel().tolist()
r=set(list(filter(lambda x: x>0,image)))
sizes=[]
for v in r:
    sizes.append(image.count(v))
value=1
for i in range(3):
    value*=max(sizes)
    sizes.remove(max(sizes))
print(f'Part B: {value}')