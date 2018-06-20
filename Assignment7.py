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