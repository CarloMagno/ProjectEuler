'''
Created on 29/11/2012

@author: Carlitos
'''
from time import time

meses={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
LUNES = 0
MARTES = 1
MIERCOLES = 2
JUEVES = 3
VIERNES = 4
SABADO = 5
DOMINGO = 6

def numDiasMes(mes,esBisiesto):
    if mes == 2 and esBisiesto == True:
        return 29
    else:
        return meses.get(mes)
    
def esDiaFinal(diaIni,mesIni,anyoIni,diaFin,mesFin,anyoFin):
    return anyoIni == anyoFin and mesIni == mesFin and diaIni == diaFin

def cuentaDomingosPrimeroDeMes(diaSem,diaIni,mesIni,anyoIni,diaFin,mesFin,anyoFin):
    res = 0
    iterac = 1
    esBisiesto = False
    
    while not esDiaFinal(diaIni,mesIni,anyoIni,diaFin,mesFin,anyoFin):
        if iterac%4 == 0: 
            esBisiesto = True
        else:
            esBisiesto = False
            
        if diaIni == 1 and diaSem == DOMINGO:
            print diaSem,"PRIMERO DE MES:",diaIni,"/",mesIni,"/",anyoIni
            res += 1
            
        diaSem = (diaSem+1)%7
        diaIni += 1
        if diaIni > numDiasMes(mesIni,esBisiesto):
            diaIni = 1
            mesIni = (mesIni%12)+1
            if mesIni == 1:
                anyoIni += 1
                iterac += 1
        print diaSem,"Dia:",diaIni,"Mes:",mesIni,"Anyo:",anyoIni
    return res

if __name__ == '__main__':
    print ">> Comienza busqueda"
    ini = time()
    res = cuentaDomingosPrimeroDeMes(diaSem=1,diaIni=1,mesIni=1,anyoIni=1901,diaFin=31,mesFin=12,anyoFin=2000)
    print "Resultado =",res,"en",time()-ini,"sg"