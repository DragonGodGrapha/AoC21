from statistics import median
with open('10.txt') as inputVals:
    inp=inputVals.read().splitlines()

"""
inp='''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''.splitlines()
"""

left=['(','{','[','<']
pair={'(':')',')':'(','<':'>','>':'<','{':'}','}':'{','[':']',']':'['}
cor=[]
rem=[]
errorPoints={')':3,']':57,'}':1197,'>':25137}
autoPoints={'(':1,'[':2,'{':3,'<':4}
for line in inp:
    isBad=False
    stack=[]
    for char in line:
        if char in left:
            stack.append(char)
        elif stack[-1]==pair[char]:
            stack.pop()
        else:
            isBad=True
            cor.append(char)
            break
        
    if not isBad:
        rem.append(stack[:])
errorScore=sum(list(map(lambda x: errorPoints[x],cor)))
print(f'Part A: {errorScore}')

autoScores=[]
for line in rem:
    lineScore=0
    line.reverse()
    for char in line:
        lineScore*=5
        lineScore+=autoPoints[char]
    autoScores.append(lineScore)

print(f'Part B: {median(autoScores)}')

