from collections import defaultdict, Counter

def polymerize(base,dic,count=1):
    for c in range(count):
        print(c)
        o=''
        for i in range(len(base)-1):
            pair=base[i:i+2]
            o+=base[i]+dic[pair]
        o+=base[-1]
        base=o
    return base

    
with open('14.txt') as inputVals:
    inp=inputVals.read().split('\n\n')
    
'''
inp="""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".split("\n\n")
'''

base=inp[0]
dic=defaultdict(str)

for e in inp[1].splitlines():
    k,_,v=e.split()
    dic[k]=v

final=polymerize(base,dic,10)
counts=[final.count(l) for l in set(final)]
print(f'Part A: {max([final.count(l) for l in set(final)])-min([final.count(l) for l in set(final)])}')

pairs=Counter(a+b for a,b in zip(base,base[1:]))
char=Counter(base)
for _ in range(40):
    temp=Counter()
    for (c1,c2),value in pairs.items():
        middle=dic[c1+c2]
        temp[c1+middle]+=value
        temp[middle+c2]+=value
        char[middle]+=value
    pairs=temp

print(f'Part B: {max(char.values())-min(char.values())}')
