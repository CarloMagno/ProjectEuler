def posicionAlfabeto(c):
	return ord(c)-64
	
def puntuacion(cadena):
	return sum([posicionAlfabeto(cadena[i]) for i in range(len(cadena))])
		
if __name__ == "__main__":
	f = open("names.txt","r")
	l = [f.readline()]
	l = l[0].split(',')
	l.sort()
	l = [l[i].split('"')[1] for i in range(len(l))]

	print sum([(i+1)*puntuacion(l[i]) for i in range(len(l))])
