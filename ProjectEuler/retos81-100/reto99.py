import re
from math import log    

def main():	
	maximo = 0.0
	num = 1
	lineaRes = 1
	mejorBase, mejorExp = 0, 0
	
	for linea in file('base_exp.txt'):
		base, exponente = linea.split(',')
		valor = int(exponente)*log(int(base))
		
		if valor > maximo:
			maximo = valor
			lineaRes = num
			mejorBase = base
			mejorExp = exponente
		
		num += 1
		
	print "Linea: ",lineaRes,"->",mejorBase,mejorExp

if __name__ == "__main__":
	main()
