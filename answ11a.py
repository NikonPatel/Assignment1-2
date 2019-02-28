#ANSWER11A
a=[1100,25,99.99,89,16]

def sorting_list(a):
	x=[]
	l=len(a)
	for i in range (l):
		y=max(a)
		x.append(y)
		a.remove(y)
	return x

A = (sorting_list(a))
print (A)
