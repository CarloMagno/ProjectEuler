import re

def trocea(string):
	"Devuelve una lista troceada por los espacios en blanco"
#	mo = re.findall("[0-9]{1}",string)
	mo = re.findall("[0-9]{2}",string)
	res = list(mo)
	for elem in range(len(res)):
		res[elem] = int(res[elem])
	return res

if __name__ == "__main__":
#	fich = open("reto18prueba","r")
	fich = open("reto18archivo","r")
	matriz = []
	entrada = fich.readline()
	while entrada != "":
#		print entrada
		matriz.append(trocea(entrada))
		entrada = fich.readline()
#	print matriz
	
	for i in reversed(range(len(matriz)-1)):
		for j in range(i+1):
#			print "Antes:",(i,j),matriz
			matriz[i][j] += max(matriz[i+1][j],matriz[i+1][j+1])
#			print "Despues:",(i,j),matriz
	print matriz[0][0]
