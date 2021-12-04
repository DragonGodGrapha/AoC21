from statistics import mode
with open('04.txt') as inputVals:
    inp=inputVals.read().split('\n\n')

"""
inp='''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''.split('\n\n')
"""

call=inp[0].split(',')
boards=inp[1:]
boardsraw=[]
for pos,board in enumerate(boards):
    board=board.splitlines()
    boardraw=[]
    for rowPos,row in enumerate(board):
        board[rowPos]=row.split()
        boardraw+=row.split()
    boardsraw.append(boardraw)
    lines=board.copy()
    for i in range(len(board[0])):
        col=[val[i] for val in board]
        lines.append(col)
    boards[pos]=lines
    
winner=''
winball=''
for r in range(5,len(call)+1):
    cur=call[:r]
    
    for pos,board in enumerate(boards):
        flag=0
        for line in board:
            if set(line).issubset(set(cur)):
                flag=1
                winner=pos
                winball=int(cur[-1])
                break
        if flag==1:break
    if flag==1:break

winboard=boardsraw[winner]
winboard=list(filter(lambda x: x not in cur,winboard))
tot=sum(list(map(int,winboard)))
print(f'Part A: {tot*winball}')

winner=''
winball=''
for r in range(5,len(call)+1):
    cur=call[:r]
    
    for pos,board in enumerate(boards):
        flag=0
        for line in board:
            if set(line).issubset(set(cur)):
                flag=1
                break
        if flag==1:
            last=boards.pop(pos)
            potwin=boardsraw.pop(pos)
    if len(boards)==0:
        winner=potwin
        winball=int(cur[-1])
        break
winboard=winner
winboard=list(filter(lambda x: x not in cur,winboard))
tot=sum(list(map(int,winboard)))
print(f'Part B: {tot*winball}')

        
