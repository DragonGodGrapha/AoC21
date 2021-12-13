
def fold(pointList,fold):
    if fold[0]=='x':axis=0
    else:axis=1
    pivot=fold[1]
    newPoints=[]
    
    for point in pointList:
        if axis==0:
            newX=(point[0] if point[0]<pivot else pivot-(point[0]-pivot))
            newY=point[1]
        else:
            newX=point[0]
            newY=(point[1] if point[1]<pivot else pivot-(point[1]-pivot))
        newPoints.append((newX,newY))
    return list(set(newPoints))


with open('13.txt') as inputVals:
    inp=inputVals.read().split('\n\n')
'''  
inp="""6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".split("\n\n")
'''
points=inp[0].splitlines()
points=list(map(lambda x: tuple(list(map(int,x.split(',')))),points))

folds=inp[1].splitlines()
folds=list(map(lambda x: x.split()[-1],folds))
folds=list(map(lambda x: (x[0],int(x[2:])),folds))
print(f'Part A: {len(fold(points,folds[0]))}')

for f in folds:
    points=fold(points,f)
height=max([point[1] for point in points])
width=max([point[0] for point in points])

for row in range(height+1):
    display=''
    for char in range(width+1):
        display+=(' ' if (char,row) not in points else '█')
    print(display)
