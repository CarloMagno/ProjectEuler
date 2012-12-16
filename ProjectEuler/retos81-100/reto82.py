'''
Created on 03/12/2012

@author: Carlitos
'''
from time import time
from AStarModule import AEstrella, Problema
from copy import deepcopy

matriz = []
LIM = 80
MIN = 999999

def inicializar():
    global MIN
    if LIM != 5:
        for line in open("matrix81.txt","r"):
            linea = [int(i) for i in line.split(',')]
            auxmin = min(linea)
            if auxmin < MIN:
                MIN = auxmin
            matriz.append(linea)
    else:
        MIN = 18
        matriz.append([131,673,234,103,18])
        matriz.append([201,96,342,965,150])
        matriz.append([630,803,746,422,111])
        matriz.append([537,699,497,121,956])
        matriz.append([805,732,524,37,331])
#    print matriz

class Nodo(Problema):
    def __init__(self, pos):
        '''
        '''
        self.pos = pos
        if self.pos[0] == -1:
            self.valor = 0
        else:
            self.valor = matriz[self.pos[0]][self.pos[1]]
          
    def __eq__(self, o):
        '''
        '''
        if self.pos[0] == -1 or o.pos[0] == -1:
            return isinstance(o, Nodo) and self.pos[1] == o.pos[1]
        else:
            return isinstance(o, Nodo) and self.pos[0] == o.pos[0] and self.pos[1] == o.pos[1]       
        #return isinstance(o, Nodo) and self.pos[1] == o.pos[1]
    
    def __str__(self):
        '''
        '''
        return str(self.pos)
    
    def estadoFinal(self):
        '''
        Devuelve el estado final que queremos alcanzar.
        @return: Problema
        '''
        return Nodo((-1,LIM-1))
    
    def heuristico(self):
        '''
        Devuelve el heuristico.
        @return: int
        '''
        #return (abs(LIM-1-self.pos[0])+abs(LIM-1-self.pos[1]))*MIN
        if self.pos[0] == -1:
            res = 0
        else:
            res = ((LIM-1)-self.pos[1])*MIN
        
        return res
    
    def hijos(self):
        '''
        Devuelve una lista con los posibles estados a partir del actual.
        @return: list<Problema>
        '''
        res = []
        if self.pos[0] == -1:
            for i in range(LIM):
                res.append(Nodo((i,0)))
        elif self.pos[1] == 0:
            res.append(Nodo((self.pos[0],self.pos[1]+1)))
        else:
            i = self.pos[0]+1
            if i < LIM:
                 res.append(Nodo((self.pos[0]+1,self.pos[1])))
            
            i = self.pos[0]-1
            if i >= 0:
                 res.append(Nodo((self.pos[0]-1,self.pos[1])))
    
            j = self.pos[1]+1     
            if j < LIM:
                 res.append(Nodo((self.pos[0],self.pos[1]+1)))

        return res
        
    def coste(self):
        '''
        Devuelve el coste de haberse movido al estado en que nos encontramos.
        @return: int
        '''
        return self.valor
    
if __name__ == "__main__":
    inicializar()
    ini = time()
    inicio = (-1,0)
    n = Nodo(inicio)
    astar = AEstrella(n)
    res = 0
    for nodo in astar.camino:
        res += nodo.problema.valor    
        print nodo.problema, nodo.problema.valor
    
    print "SUMA MINIMA =",res
    print "Tiempo =",time()-ini,"sg"
    
