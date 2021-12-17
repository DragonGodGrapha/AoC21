from math import prod

class Packet:
    def __init__(self, code):
        self.code=code
        self.pointer=0
        self.versionSum=0
        self.outputs=[]
        self.outputs+=self.analyze()
    
    def analyze(self):
        out=[]
        while self.pointer<len(self.code):
            out+=self.readSubpacket()
            if not '1' in self.code[self.pointer:]: self.pointer=len(self.code)
        return out.copy()
        
    def readSubpacket(self):
        out=[]
        version=int(self.code[self.pointer:self.pointer+3],base=2)
        self.pointer+=3
        self.versionSum+=version
        
        typeID=int(self.code[self.pointer:self.pointer+3],base=2)
        self.pointer+=3
        
        if typeID==4:
            #Literal
            bits=''
            last=False
            while not last:
                if self.code[self.pointer]!='1':last=True
                bits+=self.code[self.pointer+1:self.pointer+5]
                self.pointer+=5
            out.append(int(bits,base=2))
        else:
            lengthID=self.code[self.pointer]
            self.pointer+=1
            if lengthID=='0':
                length=int(self.code[self.pointer:self.pointer+15],base=2)
                self.pointer+=15
                sub=Packet(self.code[self.pointer:self.pointer+length])
                out+=sub.outputs.copy()
                self.versionSum+=sub.versionSum
                self.pointer+=length
                 
            else:
                count=int(self.code[self.pointer:self.pointer+11],base=2)
                self.pointer+=11
                for _ in range(count):
                    out+=self.readSubpacket()
            
            if typeID==0:
                out=[sum(out)]
            elif typeID==1:
                out=[prod(out)]
            elif typeID==2:
                out=[min(out)]
            elif typeID==3:
                out=[max(out)]
            elif typeID==5:
                out=[int(out[0]>out[1])]
            elif typeID==6:
                out=[int(out[0]<out[1])]
            elif typeID==7:
                out=[int(out[0]==out[1])]
        
        return out.copy()
    
    
with open('16.txt') as inputVals:
    inp=inputVals.read().strip() 
#inp='880086C3E88112'
i=bin(int(inp,base=16))[2:]
i=('0'*(len(inp)*4-len(i)) + i)


a=Packet(i)

print(f'Part A: {a.versionSum}')
print(f'Part B: {a.outputs[0]}')
