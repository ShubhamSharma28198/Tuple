#ques1-->
'''We represent time in a way that’s easy for us to understand.However, Python stores it in tuples. These python tuples are made of nine numbers.

TABLE-->
Index	Field			Domain of Values
0	Year (4 digits)		Ex.- 1995
1	Month			1 to 12
2	Day			1 to 31
3	Hour			0 to 23
4	Minute			0 to 59
5	Second			0 to 61 (60/61 are leap seconds)
6	Day of Week		0 to 6 (Monday to Sunday)
7	Day of Year		1 to 366 (Julian day)
8	DST			-1,0,1

It returns a string of 24 characters.
It may also take a Python time tuple as an argument.
Since the localtime() method returns a time tuple, let's use it as the argument.'''

#ques2-->
import datetime
t=datetime.datetime.now()
print("Current date and time is:",t)
print(t.strftime("%Y-%m-%d %H:%M:%S"))

#ques3-->
import datetime
d=datetime.date.today()
print(d.month)

#ques4-->
import datetime
d=datetime.date.today()
print(d.day)

#ques5-->
import datetime
d=datetime.datetime(2009,10,5,18,00)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.second)

#ques6--->
import time
localtime=time.localtime(time.time())
print("Time is-->",localtime)

#ques7-->
import math
num=int(input("enter the number"))
print(math.factorial(num))

#ques8-->
import math
num=int(input("enter the first number"))
num1=int(input("enter the first number"))
print(math.gcd(num,num1))

#ques9-->
#(a)-->
import os
print(os.getcwd())
#(b)-->
import os
s=os.getenv('path')
print(s)

'''
#output-->
#1-->

#2-->
Current date and time is: 2018-06-21 14:00:05.274219
2018-06-21 14:00:05

#3-->
6

#4-->
21

#5-->
2009
10
5
18
0

#6-->
Time is--> time.struct_time(tm_year=2018, tm_mon=6, tm_mday=21, tm_hour=14, tm_min=0, tm_sec=5, tm_wday=3, tm_yday=172, tm_isdst=0)

#7-->
enter the number5
120

#8-->
enter the first number5
enter the first number15
5

#9-->
#(a)-->
C:\Users\User\PycharmProjects\untitled1
#(b)-->
C:\Program Files (x86)\Intel\iCLS Client\;C:\Program Files\Intel\iCLS Client\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Git\cmd;C:\Program Files\Git\mingw64\bin;C:\Program Files\Git\usr\bin;C:\Users\User\AppData\Local\Programs\Python\Python36-32\Scripts\;C:\Users\User\AppData\Local\Programs\Python\Python36-32\;C:\Users\User\AppData\Local\Programs\Python\Python36\Scripts\;C:\Users\User\AppData\Local\Programs\Python\Python36\;C:\Users\User\AppData\Local\Microsoft\WindowsApps;;C:\Program Files\Microsoft VS Code\bin;C:\Users\User\PycharmProjects\untitled1\venv\Scripts
'''
