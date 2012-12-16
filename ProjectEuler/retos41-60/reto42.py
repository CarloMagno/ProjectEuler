'''
Created on 03/12/2012

@author: Carlitos
'''
from time import time

def posicionAlfabeto(c):
    return ord(c)-64
    
def puntuacion(cadena):
    return sum([posicionAlfabeto(cadena[i]) for i in range(len(cadena))])

def triangle(n):
    return n*(n+1)/2

def reto42():
    f = open("words.txt","r")
    l = [f.readline()]
    l = l[0].split(',')
    l.sort()
    l = [l[i].split('"')[1] for i in range(len(l))]
    l = map(puntuacion,l)
    
    Tset = [triangle(i) for i in range(1,10**4)]
    print len([i for i in l if i in Tset])
    
if __name__ == '__main__':
    ini = time()
    reto42()
    print "Tiempo =",time()-ini,"sg"