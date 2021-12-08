from statistics import median

with open('07.txt') as inputVals:
    inp=list(map(int,inputVals.read().split(',')))

#inp=[16,1,2,0,4,2,7,1,2,14]

mid=int(median(inp))

fuel=sum(list(map(lambda x: abs(x-mid),inp)))
print(f'Part A: {fuel}')

cum=[]

for i in range(max(inp)+1):
    cum.append(sum(list(map(lambda x: sum(range(abs(i-x)+1)),inp))))

print(f'Part B: {min(cum)}')