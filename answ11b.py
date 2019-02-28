#ANSWER11B
a= [55,58,59,32,14,6]
def min_list(a):
	z=[]
	l=len(a)
	for i in range (l):
		y=min(a)
		z.append(y)
		a.remove(y)
	return z

B = (min_list(a))
print (B)