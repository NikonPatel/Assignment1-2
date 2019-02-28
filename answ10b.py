x=[]
z=int(input('how many numbers you want in your list: '))
n=0
while n!=z:
	y=(input('enter your number: '))
	if y>8:
		pass
	else:
		x.append(y)
		n+=1
	
print(x)