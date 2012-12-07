'''
Created on 03/12/2012

@author: Carlitos
'''
from time import time

def reto40():
    d = ""
    for i in range(1,10**6+1):
        d += str(i)

    print d[0]
    print d[10-1]
    print d[100-1]
    print d[1000-1]
    print d[10000-1]
    print d[100000-1]
    print d[1000000-1]
    
    print int(d[0])*int(d[10-1])*int(d[100-1])*int(d[1000-1])*int(d[10000-1])*int(d[100000-1])*int(d[1000000-1])

if __name__ == '__main__':
    ini = time()
    reto40()
    print "Tiempo =",time()-ini,"sg"