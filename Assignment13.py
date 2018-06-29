#ques1--.
a = 3
try:
    a = a / (a - 3)
    print(a)
except ZeroDivisionError as e:
    print("Error is identify")
    print(e)

#ques2-->
try:
    l=[1,2,3]
    print(l[3])
except Exception as e:
    print("Error is identify")
    print(e)

#ques3-->
print('an exception\nNameError')

#ques4-->
print('The output is-->-5 \na/b result in zero')

#ques5-->
#a-->
try:
    from tweepy import *
except  Exception as e:
    print('The import error')
    print(e)
#b-->
x='xyz'
try:
    int(x)
except Exception as e:
    print("Value error occur")
    print(e)
#c-->
try:
    l=[1,2,3]
    print(l[3])
except Exception as e:
    print("Error is identify")
    print(e)

#ques6-->
class under_age(Exception):
    def __init__(self,age):
        self.age = age
        print('you are %d years old, please enter age above 18 to proceed'%(self.age))
def enter_age():
    try :
        x = int(input('enter your age :'))
        if x<18 :
            raise under_age(x)
        print('now you can apply for the visa...!! as you are above 18')
    except under_age as e :
        print('this is an under age error.')
        enter_age()
enter_age()

'''
#OUTPUT-->
#1-->
Error is identify
division by zero
#2-->
Error is identify
list index out of range

#3-->
an exception
NameError

#4-->
The output is-->-5 
a/b result in zero

#5-->
#a-->
The import error
No module named 'tweepy'
#b-->
Value error occur
invalid literal for int() with base 10: 'xyz'
#c-->
Error is identify
list index out of range

#6-->
enter your age :5
you are 5 years old, please enter age above 18 to proceed
this is an under age error.
enter your age :25
now you can apply for the visa...!! as you are above 18
'''

