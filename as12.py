#ASANSWER12
a={}
x = int(raw_input('enter the number till you want a dictionary of each numbers squre'))
def output(x):
	for i in range(1,x+1):
		a[i]=i*i
	
	print(a)

x = output(x)
		