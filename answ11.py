a=[3,4,7,8,2]

def sorting_list(a):
	x=[]
	l=len(a)
	for i in range (l):
		y=min(a)
		x.append(y)
		a.remove(y)
	return x
def max_list(b):
	b=[]
	l=len(a)
	for i in range (1):
		y=max(b)
		b.append(y)
		a.remove(y)
	return x
 
print (sorting_list(a))
print (sorting_list(b))