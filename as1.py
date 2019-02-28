x=int(raw_input('Enter the value till you want fibonacci :  '))
def fib(x):
	y=1
	z=1
	L=[]

	for i in range (x):
		b=y+z
		L.append(y)
		x,y=y,b
	return	(L)

normal_number=(fib(x))
print(normal_number)



cubes_of_fibo=list(map(lambda x :x*x*x,normal_number))