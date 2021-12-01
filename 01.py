with open('01.txt') as inputVals:
        inp=list(map(int,inputVals.read().splitlines()))
#inp=[199,200,208,210,200,207,240,269,260,263]

inc=0
for j in range(len(inp)-1):
    
    inc+=(1 if inp[j+1]>inp[j] else 0)
print(f'Part A: {inc}')

rinc=0
for j in range(1,len(inp)-2):
    a=sum(inp[j-1:j+2])
    b=sum(inp[j:j+3])
    rinc+=(1 if b>a else 0)
print(f'Part B: {rinc}')