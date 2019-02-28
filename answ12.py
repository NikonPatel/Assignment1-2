x=[1,2,3,4,4.5]
def dist_pair(list):
	for i in x:
		for j in x:
			if i!=j and (i*j)/2!=0:
				return True
			else:
				False
				
				
print(x,dist_pair(x))