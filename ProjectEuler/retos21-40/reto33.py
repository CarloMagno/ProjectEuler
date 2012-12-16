'''
Created on 03/12/2012

@author: Carlitos
'''
from time import time

def simplifica(num,den):
    num = float(num)
    den = float(den)
    valOrig = num/den
    
    #print "valOrig",valOrig
    
    num1 = num//10
    num2 = num%10    
    den1 = den//10
    den2 = den%10
        
    #print num1,num2,den1,den2
    
    val1,val2,val3,val4 = -1.0,-1.0,-1.0,-1.0
    
    if den1 != 0.0:
        if den2 == num1:
            val1 = num2/den1
        
        if den2 == num2:
            val2 = num1/den1
        
    if den2 != 0.0:
        if den1 == num1:
            val3 = num2/den2
        
        if den1 == num2:
            val4 = num1/den2

    vals = [val1,val2,val3,val4]
    #print vals
    if valOrig in vals:
        print num,"/",den

def reto33():
    for den in range(10,100):
        for num in range(10,den):
                if num%10!=0 or den%10!=0:
                    simplifica(num,den)

if __name__ == '__main__':
    ini = time()
    reto33()
    #simplifica(16,96)
    print "Tiempo =",time()-ini,"sg"