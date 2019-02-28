#ANSWER5
x=[1, 2, 3, 4, 5, 8, 4, 4, 4, 4, 323, 2, 56]
print x
num = {}
for numeric in x:
	if numeric not in num:
		num[numeric]=1
	else:
		num[numeric]+=1
print num	