#ASANSWER18
dic1={1:'a',2:'b'}
dic2={3:'c',4:'d'}
dic3={5:'e',6:'f'}
New_dic={}
for d in (dic1,dic2,dic3):
    New_dic.update(d)

print(New_dic)