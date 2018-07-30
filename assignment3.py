#ques1-->
class Calcus():
    def cal(self,A,B,C):    #C=p(A|B)
        return (C*B/A)
x=Calcus()
print(x.cal(11 / 36,6 / 36,2 / 36))        #return (C*B/A)---> p(B|A)

#ques2-->
'''
BAG A-> 4 White,6 Black
BAG B-> 4 White,3 Black
p(E1)=probability for selecting bag1
p(E1)=1/2
p(E1)=probability for selecting bag2
p(E1)=1/2
p(E1/A)=       1/2*6/10
           _________________
           1/2*6/10+1/2*3/7
p(E1/A)=0.58333

#ques3-->
Let A be the event that Person Obtains is a four
And, B be the event that Person doesn't Obtain is a four
P(A)= 1/6 and P(B)= 2/3
Let C be the event that Person reports that it is a four.
p(C)=p(A)* p(B)
=2/3*1/6
=2/18
=1/9

'''
