#ques1
tup1=(0,1,2,3,4,5)
print(len(tup1))

#ques2
print(max(tup1))
print(min(tup1))

#ques3
check=(1,2,3)
cont=check+check
print(cont)
mult=check*3
print(mult)

#ques4
num_set = set([1,2,3,4,5,6])
print(num_set)

#ques5
dict={'Name':'Shubham','Age':'12','Class':'V'}
print(dict['Name'])
print(dict['Class'])

#ques6
mydict = {'Ram':40,'Ravi':2,'Bhavesh':1,'Dr':3}

for key in sorted (mydict.keys()):
 print("%s: %s" % (key, mydict[key]))

#ques7
import collections
a='MISSISSIPPI'
print(collections.Counter(a))




