#ques1-->
list_1=[]
for i in range(0,10):
    y = int(input("enter the element"))
    list_1.append(y)
print(list_1)

#ques2-->
a=int(input("enter the no:"))
a=1
while(a<10):
    print(a)

#ques3
list_1=[]
for i in range(0,10):
    num=int(input("enter the element"))
    list_1.append(num)
print("list_1 is-->",list_1)
list_2=[]
for i in list_1:
    i=i*i
    list_2.append(i)
print("The new list is--> ",list_2)

#ques4
list_3=[1,2,3,'4','5','6',4.5,1.2,2.5]
list_int=[x for x in list_3 if isinstance(x,int)]
print(list_int)
list_str=[x for x in list_3 if isinstance(x,str)]
print(list_str)
list_float=[x for x in list_3 if isinstance(x,float)]
print(list_float)


#ques5
#for even numbers--->
list_1=[]
for ele in range(0,101,2):
    list_1.append(ele)
print("list is-->", list_1)
#for odd numbers--->
list_2=[]
for ele in range(1,101,2):
    list_2.append(ele)
print("list is-->", list_2)


#ques6
x=4
for ele in range(x):
    ele=ele+1
    print('*'*ele)



#ques7
#Create a user defined dictionary and get keys corresponding to the value using for loop.
mydict = {'Ram':40,'Ravi':2,'Bhavesh':1,'Dr':3}
for key in mydict.keys():
    print(key,mydict[key])

    #OUTPUT---->
#1--->
enter the element0
enter the element1
enter the element2
enter the element3
enter the element4
enter the element5
enter the element6
enter the element7
enter the element8
enter the element9
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#2-->
1
1
1
1
1
1
1
1
1
1
upto infinity

#3--->
enter the element0
enter the element1
enter the element2
enter the element3
enter the element4
enter the element5
enter the element6
enter the element7
enter the element8
enter the element9
list_1 is--> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
The new list is-->  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#4--->
[1, 2, 3]
['4', '5', '6']
[4.5, 1.2, 2.5]

#5--->
list is--> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
list is--> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]

#6--->
*
**
***
****

#7-->
Ram 40
Ravi 2
Bhavesh 1
Dr 3


