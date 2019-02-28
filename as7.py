#ASANSWER7
odd_num=[]
def odd(n):
	count=0
	for i in range(1,100):
		if i%2==0:
			pass
		else:
			count=count+1
			odd_num.append(i)

odd(100)
#print(odd_num)
print('The list of first 30 odd number is below')
first30_oddnum=odd_num[:30]
print(first30_oddnum)
sum_odd=reduce(lambda x,y:x+y, first30_oddnum)
print('The total sum of the first 30 odd number is :',sum_odd)