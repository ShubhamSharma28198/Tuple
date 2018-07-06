import pandas as pd
a={'name':pd.Series(['Shubham']),
   'age':pd.Series([21]),
   'mail_id':pd.Series(['shubham098089@gmail.com']),
   'phone':pd.Series([1234567890])
}
df=pd.DataFrame(a)
print(df)
b={'name':pd.Series(['sharma']),
   'age':pd.Series([20]),
   'mail_id':pd.Series(['sharma098089@gmail.com']),
   'phone':pd.Series([9876543210])
}
df2=pd.DataFrame(b)
df3=df.append(df2)
print("new data will be added:")
print(df3)

#ques2-->
import csv
import pandas as pd
a=pd.read_csv('weather.csv')
print(a)

#1-->
print("First 5 rows",a.head(5))

#2-->
print("First 10 rows",a.head(10))

#3-->
df=pd.DataFrame(a)
print(df.describe(include='all'))

#4-->
print("last 5 rows",a.tail(5))

#5-->
b=df.loc[0]
print("Extract 2 column",b)
df=pd.DataFrame(b)
print(df.describe(include='all'))
