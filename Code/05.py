from collections import defaultdict
import re
from math import gcd


def makeline(pos1,pos2,diag=0):
    if diag==0 and (pos1[0]!=pos2[0] and pos1[1]!=pos2[1]):
        return []
    line=[]
    delX=pos2[0]-pos1[0]
    delY=pos2[1]-pos1[1]
    delX,delY=(delX/gcd(delX,delY),delY/gcd(delX,delY))
    delX=int(delX)
    delY=int(delY)
    while pos1!=pos2:
        line.append([pos1[0],pos1[1]])
        pos1[0]+=delX
        pos1[1]+=delY
    line.append(pos2)
    return line

with open('05.txt') as inputVals:
    inp=inputVals.read().splitlines()

"""inp='''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''.splitlines()"""


exp=re.compile('(\d+),(\d+) -> (\d+),(\d+)')
points=defaultdict(int)
diagpoints=defaultdict(int)
for line in inp:
    pos1=list(map(int,exp.search(line).group(1,2)))
    pos2=list(map(int,exp.search(line).group(3,4)))
    for point in makeline(pos1.copy(),pos2.copy()):
        points[tuple(point)]+=1
        
    for point in makeline(pos1.copy(),pos2.copy(),diag=1):
        diagpoints[tuple(point)]+=1
        
print(f'Part A: {len(list(filter(lambda x:x>1,list(points.values()))))}')
print(f'Part B: {len(list(filter(lambda x:x>1,list(diagpoints.values()))))}')

