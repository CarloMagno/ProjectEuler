'''
Created on 03/12/2012

@author: Carlitos
'''
from time import time
    
#def sumaCuadradaDigitos(n):
#    return sum([int(c)**2 for c in str(n)])

def sumaCuadradaDigitos(n):
    s = 0
    while n:
        s += (n%10)**2
        n = n//10
    return s

def reto92():
    # Inicializar registro de cadenas.
    registro = [0]*568 # 567 es el peor caso ya que f(9.999.999) = 567 
    for aux in range(2,568):
        num = aux
        while num != 1:
            num = sumaCuadradaDigitos(num)
            if num == 89:
                registro[aux] = 1
                break
        print aux
        
    print "Fin inicializacion."
    raw_input()
    res = 0
    for i in range(1,10**7):
        num = sumaCuadradaDigitos(i)
        if registro[num] == 1:
            res += 1
        if i%100000 == 0: 
            print i
    print "Resultado =", res
    
if __name__ == '__main__':
    ini = time()
    reto92()
    print "Tiempo =",time()-ini,"sg"