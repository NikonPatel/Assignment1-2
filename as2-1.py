x=int(raw_input('enter the number that long you want fibonachi series:  '))
def fib(x):
	a=1
	b=1
	L=[]

	for i in range (x):
		c=a+b
		L.append(a)
		a,b=b,c
	return	(L)

normal_number=(fib(x))
print(normal_number)

# higher order function lambda

cub_of_fib=list(map(lambda x :x*x*x,normal_number))

print(cub_of_fib)
