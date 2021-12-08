

with open('08.txt') as inputVals:
    inp=inputVals.read().splitlines()
"""
inp='''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''.splitlines()
"""
#inp=['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']


outRaw=[]
outDecode=[]

for j in inp:
    out=j.split('|')[1].split()
    outRaw+=out
countUnique=len(list(filter(lambda x: len(x) in [2,3,4,7],outRaw)))
print(f'Part A: {countUnique}')

for j in inp:
    test,out=list(map(lambda x: x.split(),j.split('|')))
    out=[set(i) for i in out]
    test=[set(i) for i in test]
    numDict={}
    one=list(filter(lambda x: len(x)==2,test))[0]
    four=list(filter(lambda x: len(x)==4,test))[0]
    seven=list(filter(lambda x: len(x)==3,test))[0]
    eight=list(filter(lambda x: len(x)==7,test))[0]
    fivedigit=list(filter(lambda x: len(x)==5,test))
    sixdigit=list(filter(lambda x: len(x)==6,test))
    
    nine=(set.union(four,seven))
    for k in sixdigit:
        if nine.issubset(k):
            nine=k
            break
    sixdigit.remove(nine)
    
    for k in sixdigit:
        if one.issubset(k):
            zero=k
            break
    sixdigit.remove(zero)
    six=sixdigit.pop()
    bitC=set.difference(eight,six)
    
    for k in fivedigit:
        if one.issubset(k):
            three=k
            break
    fivedigit.remove(three)
    
    for k in fivedigit:
        if bitC.issubset(k):
            two=k
            break
    fivedigit.remove(two)
    five=fivedigit.pop()
    
    numDict[frozenset(zero)]='0'
    numDict[frozenset(one)]='1'
    numDict[frozenset(two)]='2'
    numDict[frozenset(three)]='3'
    numDict[frozenset(four)]='4'
    numDict[frozenset(five)]='5'
    numDict[frozenset(six)]='6'
    numDict[frozenset(seven)]='7'
    numDict[frozenset(eight)]='8'
    numDict[frozenset(nine)]='9'
    
    outDecoded=''
    for k in out:
        outDecoded+=numDict[frozenset(k)]
    outDecode.append(int(outDecoded))
    
print(f'Part B: {sum(outDecode)}')
    
    
    
    
    