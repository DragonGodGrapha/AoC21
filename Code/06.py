def populate(count):
    mid={}
    for j in range(8):
        mid[j]=count[j+1]
    mid[8]=count[0]
    mid[6]=mid[6]+count[0]
    return mid

with open('06.txt') as inputVals:
    inp=list(map(int,inputVals.read().split(',')))


#inp=[3,4,3,1,2]
counter={}
for j in range(9):
    counter[j]=inp.count(j)

for i in range(256):
    counter=populate(counter)
    if i==79:
        partA=sum(list(counter.values()))
print(f'Part A: {partA}')
print(f'Part B: {sum(list(counter.values()))}')