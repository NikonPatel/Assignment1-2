#ASANSWER5
string="innovationwithpython"
len=len(string)
print (len)
even_alpha=[]
for i in range(len):
	if i%2==0:
		even_alpha.append(string[i])

print(even_alpha)
print(''.join(even_alpha))