from statistics import mode
with open('03.txt') as inputVals:
    inp=inputVals.read().splitlines()

#inp=['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

gamma=''
epsilon=''

for i in range(len(inp[0])):
    b=int(mode([val[i] for val in inp]))
    gamma+=str(b)
    epsilon+=str(int(not b))
    

print(f'Part A: {int(gamma,base=2)*int(epsilon,base=2)}')

inp_c=inp.copy()
for i in range(len(inp[0])):
    
    b= ('1'if list.count([val[i] for val in inp_c],'1')>=len(inp_c)/2 else '0')
    inp_c=list(filter(lambda x:x[i]==b,inp_c))
    if len(inp_c)==1:break

ox=inp_c[0]

inp_c=inp.copy()
for i in range(len(inp[0])):
    
    b= ('0'if list.count([val[i] for val in inp_c],'1')>=len(inp_c)/2 else '1')
    inp_c=list(filter(lambda x:x[i]==b,inp_c))
    if len(inp_c)==1:break
    
co=inp_c[0]
print(f'Part A: {int(ox,base=2)*int(co,base=2)}')