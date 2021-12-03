class Sub:
    def __init__(self,name="Sub",debug=0):
        self.posX=0
        self.posY_p=0
        self.posY_v=0
        self.aim=0
        self.name=name
        
    def forward(self,val):
        self.posX+=val;
        self.posY_v+=(self.aim*val)
        
    def down(self,val):
        self.posY_p+=val;
        self.aim+=val;
        
    def up(self,val):
        self.posY_p-=val;
        self.aim-=val;
        

with open('02.txt') as inputVals:
        inp=inputVals.read().splitlines()


#inp=['forward 5','down 5','forward 8','up 3','down 8','forward 2']
sub=Sub()
for inst in inp:
    d,v=inst.split()
    t='sub.'+d+'('+v+')'
    eval(t)

print(f'Part A: {sub.posX*sub.posY_p}')
print(f'Part B: {sub.posX*sub.posY_v}')