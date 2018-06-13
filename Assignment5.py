#ques1-->
year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

#ques2-->
length=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))

if(length==breadth):
    print("it is a square")
else:
    print("It is a rectangle")


#ques3-->
person1=int(input("enter the age of person1:"))
person2=int(input("enter the age of person2:"))
person3=int(input("enter the age of person3:"))
# for oldest
if(person1>person2 and person1 > person3):
        print("person1 is oldest")
elif(person2 > person1 and person2 > person3):
        print("person2 is oldest")
elif(person3 > person1 and person3 > person3):
        print("person3 is oldest")
        #the youngest one
if(person1 < person2 and person1 < person3):
    print("person1 is youngest")
elif(person2 < person1 and person2 < person3):
    print("person2 is youngest")
elif(person3 < person1 and person3 < person1):
        print("person3 is youngest")

#ques4-->
points=int(input("enter the value of points"))
if(points<=50):
    print("Sorry! No prize this time.")
elif(points>50 and points<=150):
    print("Congratulations! You won a  Wooden Dog")
elif(points>151 and points<=180):
    print("Congratulations! You won a  Book")
elif(points>181 and points<=200):
    print("Congratulations! You won a  Chocolates")


#ques5-->
item=int(input("enter the no. of item"))
cost=item*100
if(cost>=1000):
    print("10% discount on item")
else:
    print("No discount on the item")
discount=cost-cost*.1
print(discount)


#output
Enter a year: 2000
2000 is a leap year
enter the length:5
enter the breadth:5
it is a square
enter the age of person1:7
enter the age of person2:6
enter the age of person3:5
person1 is oldest
person3 is youngest
enter the value of points155
Congratulations! You won a  Book
enter the no. of item15
10% discount on item
1350.0
