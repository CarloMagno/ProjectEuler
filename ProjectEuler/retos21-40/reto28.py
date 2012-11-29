m = []
tam = 1001
num = 1
for i in range(tam):
	m1 = []
	for j in range(tam):
		m1.append(0)
	m.append(m1)

i,j=(tam-1)/2,(tam-1)/2	

lu = (i-1,j-1)
ld = (i+1,j-1)
ru = (i-1,j+1)
rd = (i+1,j+1)

m[i][j] = num
num += 1
j += 1

#print lu,ld,ru,rd

while num < tam*tam+1:
	while i<rd[0]:
	#	print num,":",i,j
		m[i][j] = num
		num += 1
		if num > tam*tam: break
		i += 1

	while j>ld[1]:
	#	print num,":",i,j
		m[i][j] = num
		num += 1
		if num > tam*tam: break
		j -= 1
	
	while i>lu[0]:
	#	print num,":",i,j
		m[i][j] = num
		num += 1
		if num > tam*tam: break
		i -= 1
	
	while j<=ru[1]:
	#	print num,":",i,j
		m[i][j] = num
		num += 1
		if num > tam*tam: break
		j += 1
	
#	print "Muevo indices"

	lu = (lu[0]-1,lu[1]-1)
	ld = (ld[0]+1,ld[1]-1)
	ru = (ru[0]-1,ru[1]+1)
	rd = (rd[0]+1,rd[1]+1)
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
suma = 0

for i in range(tam):
	suma += m[i][i]
	suma += m[(tam-1)-i][i]
	
suma -= m[(tam-1)/2][(tam-1)/2]
print suma
