#ASANSWER6
numbers=[]
def number(x):
	for i in range(1,x-1):
		if i%2==0 and i%6==0:
			numbers.append(i)

x=number(50)
print(numbers)
sum_of_last_three =sum(numbers[-3:])
print('the total of last three digit is:',sum_of_last_three) 