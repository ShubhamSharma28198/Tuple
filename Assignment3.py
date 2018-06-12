#ques1
list1=[]
Name1=input("Enter the name:")
list1.append(Name1)
print("This list is",list1)

#ques2
list2=[]
Name1=input("Enter the name:")
list2.append(Name1)
fruits=('apple','orange','banana')
list2.append(fruits)
print("This final list is",list2)

#ques3
A=['1','2','1','4','1','3','2','4']
A1=A.count('1')
print(A1)

#ques4
A.sort()
print(A)

#ques5
list2=['apple','orange','banana']
list3=['shirt','geans','shoes']
list4=list2+list3
print("The final list is",list4)

#ques6
#stack-->
s = ['apple','orange','banana']
s.append("grapes")
s.append("Blueberry")
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
#Queue-->
s.append("grapes")
print(s)
s.append("Blueberry")
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)

#ques7
A=('0','1','2','3','4','5')
print(A[0:6:2])
print(A[1:6:2])