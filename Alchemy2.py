import math
from fractions import Fraction
import random
frac = Fraction
inf = math.inf

class Tank:
    def __init__(self):
        self.data={}
    def add(self,name,amt):
        self.data[name]=self.data.get(name,0)+frac(amt)
    def pop(self,name):
        amt = self.data[name]
        del self.data[name]
        return amt
    def remove(self, name, amt):
        currAmt = self.data[name]
        nAmt = currAmt - frac(amt)
        if nAmt == 0:
            del self.data[name]
        else:
            self.data[name] = nAmt
    def get(self,name):
        amt = self.data[name]
        return amt
    def removeRatio(self,pairs):
        lim = inf
        for (name,rate) in pairs:
            tarAmt = self.get(name) / rate
            lim = min(lim,tarAmt)
        for (name,rate) in pairs:
            self.remove(name,lim*rate)
        return lim
    

def brk(x):
    test = math.ceil(math.sqrt(x))
    while x//test != x/test:
        test+=1
    rem = int(x/test)
    if rem == 1:
        return [x]
    else:
        return [test]+brk(rem)

def genChem(dif=1):
    global chems
    run=True
    ochems=chems[:]
    while run:
        o={}
        ck=dif//2+random.randint(2,2+dif)
        cs=random.choices(atns,range(26,0,-1),k=ck)
        for c in cs:
            o[c]=random.randint(1,2+dif)
        cm=(set(o.keys()),o)
        chems.append(cm)
        tt=react({repr(cm):1})
        if tt==[(cm,1)]:
            run=False
        else:
            del chems[-1]

random.seed(hash('Test 1'))
atns=list('abcdefghijklmnopqrstuvwxyz')
chems=[]
