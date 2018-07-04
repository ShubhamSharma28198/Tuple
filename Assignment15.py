#ques1-->
import re
emails = re.split('[@.]',"zuck26@facebook.com")
emails1=re.split('[@.]',"page33@google.com")
emails2=re.split('[@.]', "jeff42@amazon.com")
print(emails)
print(emails1)
print(emails2)

#ques2-->
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
ele=re.findall(r'[bB]\w+',text)
print(ele)

#ques3-->
sentence = "A, very very; irregular_sentence"
ele=re.sub('[\W_]',' ',sentence)
print(ele)


#ques4-->
tweet = "'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today'"
x=re.sub('!.{17}','',tweet)
print(x)

#OUTPUT-->
#1-->
['zuck26', 'facebook', 'com']
['page33', 'google', 'com']
['jeff42', 'amazon', 'com']
#2-->
['Betty', 'bought', 'bit', 'butter', 'But', 'butter', 'bitter', 'bought', 'better', 'butter', 'bitter', 'butter', 'better']
#3-->A  very very  irregular sentence
#4-->'Good adviceWhat I would do differently if I was learning to code today'
