#ques1-->
class Circle():
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        print(3.14*self.radius*self.radius)
    def getcircumference(self):
        print(self.radius*2*3.14)
x=Circle(5)
print("The radius is",x.radius)
x.getArea()
x.getcircumference()

#ques2-->
class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display(self):
        print(self.name)
        print(self.roll_no)
x=Student('RAM',22)
print(x.name)
print(x.roll_no)


#ques3-->
class Temperature():
    def convertFahrenheit(self,celsius):
        return (celsius * (9 / 5)) + 32
    def convertCelsius(self,farenhiet):
        return(farenhiet - 32) * (5 / 9)
x=Temperature()
print(x.convertFahrenheit(5))
print(x.convertCelsius(5))

#ques4-->
class Movie_detailes:
    def __init__(self,movie_name,artist_name,release_date,rating):
        self.movie_name=movie_name
        self.artist_name=artist_name
        self.release_date=release_date
        self.rating=rating
    def display(self):
        print("Movie name is->", self.movie_name)
        print("Artist name is->", self.artist_name)
        print("Release_date is->", self.release_date)
        print("rating is-->",self.rating)
    def update(self,m,a,d):
        print("updated detailes of movie:-->")
        self.movie_name=m
        self.artist_name=a
        self.release_date=d
        print("Movie name is->",self.movie_name)
        print("Artist name is->", self.artist_name)
        print("Release_date is->", self.release_date)
x=Movie_detailes('pk','amir','July 5 2017',4.7)
print(x.display())
print(x.update('IP MAN','Rock','Jan 25 2018'))


#ques5-->
class Expenditure:
    def __init__(self,expenditure,saving):
        self.expenditure=expenditure
        self.saving=saving
    def display(self):
        print(self.expenditure)
        print(self.saving)
    def total_salary(self):
        print("Total salary is-->",self.expenditure + self.saving)
x=Expenditure(55,56)
print(x.display())
print(x.total_salary())


'''
#output-->
#1-->
The radius is 5
78.5
31.400000000000002

#2-->
RAM
22

#3-->
41.0
-15.0

#4-->
Movie name is-> pk
Artist name is-> amir
Release_date is-> July 5 2017
rating is--> 4.7
updated detailes of movie:-->
Movie name is-> IP MAN
Artist name is-> Rock
Release_date is-> Jan 25 2018

#5-->
55
56
Total salary is--> 111
'''