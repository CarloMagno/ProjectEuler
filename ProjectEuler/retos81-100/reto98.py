
def sonAnagramas(str1,str2):
	l1,l2 = list(str1), list(str2)
	l1.sort()
	l2.sort()

	if l1 == l2:
		return True
	else:
		return False

if __name__ == "__main__":
	fichero = open("words.txt","r")
	nombres = fichero.read()
	nombres = nombres.replace('"',"")
	nombres = nombres.replace(',','\n')
	nombres = nombres.split('\n')

	listaCribada = []
	for i in range(len(nombres)):
		for j in range(i+1, len(nombres)):
		  if sonAnagramas(nombres[i], nombres[j]):
				listaCribada.append(nombres[i])
				listaCribada.append(nombres[j])
		          
	listaCribada = set(listaCribada)
	print listaCribada
