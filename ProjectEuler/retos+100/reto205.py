'''
Created on 03/12/2012

@author: Carlitos
'''
from time import time
import math

dictPeter = {9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,
             23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0,32:0,33:0,34:0,35:0,36:0}
dictColin = {6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,
             23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0,32:0,33:0,34:0,35:0,36:0}


def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def inicializar():
    for a in range(1,7):
        for b in range(1,7):
            for c in range(1,7):
                for d in range(1,7):
                    for e in range(1,7):
                        for f in range(1,7):
                            val = a+b+c+d+e+f 
                            dictColin[val] += 1.0

    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                for d in range(1,5):
                    for e in range(1,5):
                        for f in range(1,5):
                            for g in range(1,5):
                                for h in range(1,5):
                                    for i in range(1,5):
                                        val = a+b+c+d+e+f+g+h+i 
                                        dictPeter[val] += 1.0
#    print dictPeter
#    print dictColin

def reto205():    
    inicializar()
    
    pos = 4**9*6**6
    res = 0.0
    
    for p in dictPeter.keys():
        for c in dictColin.keys():
            if p>c:
                probP = float(dictPeter.get(p))
                probC = float(dictColin.get(c))
                res += (probP*probC)/float(pos)
    
    print "Resultado =",res            
    
if __name__ == '__main__':
    ini = time()
    reto205()
    print "Tiempo =",time()-ini,"sg"