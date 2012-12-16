'''
Created on 12/07/2012

@author: carlitos
'''
import time

class Nodo:
    '''
    Nodo de los que se sirve AEstrella.
    '''
    def __init__(self, problema, coste=0, padre=None):
        '''
        Constructor.
        '''
        self.problema = problema # Estado del problema.
        self.padre = padre
        if self.padre == None:
            self.g = coste
        else:
            self.g = coste + self.padre.g
        
        self.h = self.problema.heuristico()
        self.f = self.h + self.g
    
    def hijos(self):
        return [Nodo(problema, problema.coste(), self) for problema in self.problema.hijos()]
    
    def __eq__(self, o):
        '''
        Delegamos la igualdad entre estados al problema.
        '''
        return isinstance(o,Nodo) and self.problema == o.problema
    
    def __str__(self):
        '''
        Delegamos el toString al problema.
        '''
        return str(self.problema)
    
class AEstrella:
    '''
    Algoritmo AEstrella.
    '''
    def __init__(self, problema):
        '''
        Constructor.
        '''
        self.problema = problema
        
        self.inicio = Nodo(problema,problema.coste())
        self.fin = Nodo(problema.estadoFinal())
        
        self.abierta = []
        self.cerrada = []
        
        self.cerrada.append(self.inicio)
        
        self.abierta += self.inicio.hijos()
        self.iter = 0
        start_time = time.time()
        while self.objetivo():
            self.buscar()
            self.iter += 1
        
        self.total_time = time.time() - start_time    
        self.camino = self.camino()
        
    # toString de la solucion.
    def __str__(self):
        res = ""
        for p in self.camino:
            res += str(p)
            res += "\n"
        return res
    
    # Devuelve un string con estadisticas.
    def stats(self):
        res = ""
        #res += "Nodos en abierto:"+str(len(self.abierta))+"\n"
        res += "Caminos explorados: "+str(len(self.cerrada))+"\n"
        res += "Iteraciones: "+str(self.iter)+"\n"
        res += "Movimientos: "+str(len(self.camino)+1)+"\n"
        res += "Coste: "+str(self.cerrada[-1].f)+"\n"
        res += "Tiempo: "+str(self.total_time)+"segundos\n"
        return res
        
    # Comprueba si un nodo esta en la lista.
    def en_lista(self, nodo, lista):
        for i in range(len(lista)):
            if nodo == lista[i]:
                return 1
        return 0
    
    # Gestiona los vecinos del nodo seleccionado.
    def ruta(self):
        for i in range(len(self.nodos)):
            if self.en_lista(self.nodos[i], self.cerrada):
                for j in range(len(self.abierta)):
                        if self.nodos[i] == self.abierta[j]:
                            del self.abierta[j]
                            self.abierta.append(self.nodos[i])
                            break
            elif not self.en_lista(self.nodos[i], self.abierta):
                self.abierta.append(self.nodos[i])
            else:
                if self.select.g > self.nodos[i].g:
                    for j in range(len(self.abierta)):
                        if self.nodos[i] == self.abierta[j]:
                            del self.abierta[j]
                            self.abierta.append(self.nodos[i])
                            break 
                           
    # Pasa el elemento de f menor de la lista abierta a la cerrada.
    def f_menor(self):
        a = self.abierta[0]
        n = 0
        for i in range(1, len(self.abierta)):
            if self.abierta[i].f < a.f:
                a = self.abierta[i]
                n = i
        #print a.problema,a.problema.valor,"-> f=",a.f,"-> g=",a.g,"-> h=",a.h
        self.cerrada.append(self.abierta[n])
        del self.abierta[n]

    # Analiza el ultimo elemento de la lista cerrada.    
    def buscar(self):
        self.f_menor()
        self.select = self.cerrada[-1]
        self.nodos = self.select.hijos()
        self.ruta()
#        print "SELECCIONADO:",(str(self.select),self.select.f)
#        print "HIJOS:",[(str(n),n.f) for n in self.nodos]
#        print "ABIERTOS:",[(str(n),n.f) for n in self.abierta]
#        print "CERRADOS:",[(str(n),n.f) for n in self.cerrada]        
#        print "-----------------------------"

        
    # Comprueba si el objetivo objetivo esta en la lista abierta.    
    def objetivo(self):
        for i in range(len(self.abierta)):
            if self.fin == self.abierta[i]:
                return 0
        return 1    
    
    # Retorna una lista con el camino solucion.    
    def camino(self):
        for i in range(len(self.abierta)):
            if self.fin == self.abierta[i]:
                objetivo = self.abierta[i]
                
        camino = []
        while objetivo != None:
            camino.append(objetivo)
            objetivo = objetivo.padre
        camino.reverse()
        return camino
     
class Problema:
    '''
    Representacion de un problema. REDEFINIR __eq__ y __str__. Interfaz.
    '''
    def __init__(self):
        '''
        '''
        raise NotImplementedError()
    
    def __eq__(self, o):
        '''
        '''
        raise NotImplementedError()
    
    def __str__(self):
        '''
        '''
        raise NotImplementedError()
    
    def estadoFinal(self):
        '''
        Devuelve el estado final que queremos alcanzar.
        @return: Problema
        '''
        raise NotImplementedError()
    
    def heuristico(self):
        '''
        Devuelve el heuristico.
        @return: int
        '''
        raise NotImplementedError()
    
    def hijos(self):
        '''
        Devuelve una lista con los posibles estados a partir del actual.
        @return: list<Problema>
        '''
        raise NotImplementedError()
    
    def coste(self):
        '''
        Devuelve el coste de haberse movido al estado en que nos encontramos.
        @return: int
        '''
        raise NotImplementedError()
    