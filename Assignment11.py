#ques1-->
import time
import threading
class thread(threading.Thread):
    def __init__(self,delay):
        threading.Thread.__init__(self)
        self.delay=delay

    def show(self):
        time.sleep(self.delay)

    def run(self):
        print("The process is started")
        self.show()
start=time.time()
th=thread(5)
th.start()
th.join()
end=time.time()
print("The process is ended")

#ques2-->
import time
import threading
class number(threading.Thread):
    def __init__(self,delay):
        threading.Thread.__init__(self)
        self.delay=delay
    def show(self):
        time.sleep(self.delay)
    def run(self):
        for i in range(1,11):
            print(i)
            self.show()
n=number(1)
n.start()
n.join()
print("The process is ended")

#ques3-->
import time
import threading
class thread(threading.Thread):
    def __init__(self,delay):
        threading.Thread.__init__(self)
        self.delay=delay
    def show(self):
        start=time.time()
        delay=2*self.delay
        time.sleep(delay)
        self.delay=self.delay+1
        end=time.time()
        print("Time delay between two element are:",int(end-start,))
    def list(self):
        list=['1','2','3','4','5','6','7','8','9']
        for i in list:
            thread.show(self)
            print(i)
    def run(self):
        self.list()
th=thread(1)
th.start()
th.join()
print("The process is ended")


#ques4-->
import time
import threading
from math import factorial
class fact(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num=num
    def factorial(self):
        return(factorial(num))
    def show(self):
        print(self.factorial)
    def run(self):
        self.factorial(self)
num=int(input("Enter the number-->"))
x=fact('num')
x.factorial()
print("the factorial of number is-->",x.factorial())

'''
#OUTPUT-->
The process is started
The process is ended

#2-->
1
2
3
4
5
6
7
8
9
10
The process is ended

#3-->
Time delay between two element are: 2
1
Time delay between two element are: 4
2
Time delay between two element are: 6
3
Time delay between two element are: 8
4
Time delay between two element are: 10
5
Time delay between two element are: 12
6
Time delay between two element are: 14
7
Time delay between two element are: 16
8
Time delay between two element are: 18
9
The process is ended


#4-->
Enter the number-->5
the factorial of number is--> 120
'''

