#ques1-->
Pi=3.14
r1=int(input("enter the radius-->"))
def area(Pi,r1):
    area = Pi * r1*2
    return area
print("The area is",area(Pi,r1))

#ques2-->
def perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False
for i in range(1,1001):
    if perfect_number(i):
        print(i)

#ques3-->
def times_tables(n, t=1):
    if t == 13:
        return
    print(str(n) + " x " + str(t) + " = " + str(n*t))
    times_tables(n, t+1)
times_tables(int(input("Enter number: ")))

#ques4-->
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))

#ques5-->
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))
dict={n:factorial(n)}
print(dict)

#output-->

#1-->
enter the radius-->2
The area is 12.56

#2-->
6
28
496


#3-->
Enter number: 12
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120
12 x 11 = 132
12 x 12 = 144


#4-->
Enter base: 5
Enter exponential value: 5
Result: 3125
Enter number:5


#5-->
Factorial:5
120
{5: 120}