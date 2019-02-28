
x=int(raw_input('How many even number you wants in your list: '))
result=[]
def even(x):
	i=1
	while i<=x:
		n=i*2
		i=i+1
		result.append(n)

y=even(x)
print(result)
result1=reduce(lambda x,y:x*y,result)

print('The mulltipication of your list is',result1)