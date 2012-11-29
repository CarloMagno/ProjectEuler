"""
What is the greatest product of four adjacent numbers in
any direction (up, down, left, right, or diagonally) in the 20x20 grid?
"""
import re
import threading

def trocea(string):
	"Devuelve una lista troceada por los espacios en blanco"
	mo = re.findall("[0-9]{2}",string)
	res = list(mo)
#	print res
	return res
	
if __name__ == "__main__":
	fichero = open("reto11archivo","r")
	entrada = fichero.readline()
	matriz = []
	while entrada != "":
#		print entrada
		matriz.append(trocea(entrada))
		entrada = fichero.readline()
#	print matriz
	maximo = 0
	for i in range(len(matriz)-3):
		for j in range(len(matriz)-3):
			prodf = 1
			prodc = 1
			prodd1 = 1
			prodd2 = 1
			for k in range(4):
				prodf = prodf * int(matriz[i][j+k])
				prodc = prodc * int(matriz[i+k][j])
				if i < (len(matriz)-3):
					prodd1 = prodd1 * int(matriz[i+k][j+k])
				if i > 3:
					prodd2 = prodd2 * int(matriz[i+k][j-k])
			maximo = reduce(max,[maximo,prodf,prodc,prodd1,prodd2])
	print maximo
