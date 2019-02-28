#ASANSWER16
x=input('Enter any  word or sentence: ')
y=input('Enetr one more different word or sentence: ')
similar = list(set([a for a in x if a in y]))
print(similar)