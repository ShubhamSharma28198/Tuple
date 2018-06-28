'''
#ques1-->
An access token is an object that describes the security context of a process or thread. The information in a token includes the identity and privileges of the user account associated with the process or thread.
When a user logs on, the system verifies the user's password by comparing it with information stored in a security database. If the password is authenticated, the system produces an access token.
Every process executed on behalf of this user has a copy of this access token.

The system uses an access token to identify the user when a thread interacts with a securable object or tries to perform a system task that requires privileges. Access tokens contain the following information:

1.The security identifier (SID) for the user's account
2.SIDs for the groups of which the user is a member
3.A logon SID that identifies the current logon session
4.A list of the privileges held by either the user or the user's groups
5.An owner SID
6.The SID for the primary group
7.The default DACL that the system uses when the user creates a securable object without specifying a security descriptor
8.The source of the access token
9.Whether the token is a primary or impersonation token
10.An optional list of restricting SIDs
11.Current impersonation levels

#ques2
facebook=151.101.65.121  #ip address
Google-->
Google uses the following public IP address ranges:

64.233.160.0 – 64.233.191.255
66.102.0.0 – 66.102.15.255
66.249.64.0 – 66.249.95.255
72.14.192.0 – 72.14.255.255
74.125.0.0 – 74.125.255.255
209.85.128.0 – 209.85.255.255
216.239.32.0 – 216.239.63.255

Only certain addresses from Google's pool work at any given time depending on how Google chooses to deploy its web server network, which is why a random example above one of these ranges may or may not work for you at a specific time.
When you find an IP address that works for you, make a note of it for future use.

Why You Might Want Google's IP Address-->
If all is working normally, you can visit the Google search engine at Google.com.
However, it's also possible to reach it using one of Google's IP addresses, even when the domain can't be reached by name.

If there's an issue with DNS, and Google's IP address can't be found by entering "google.com," you can instead enter the URL as a valid IP address in the form http://74.125.224.72/.
Some IP addresses work better than others depending on your locale.
Testing connections to websites by addresses instead of names can be a helpful troubleshooting step to verify whether the connection has an issue with name resolution rather than some other kind of technical glitch.
Also, website administrators are often curious to know when Google web crawlers visit their sites.
Analyzing web server logs reveals the IP addresses of crawlers but not their domains.

#ques3-->
import tweepy
consumer_key = '7EyzTcAkINVS3T2pb165'
consumer_secret = 'a44R7WvbMW7L8I656Y4l'
access_token = 'z00Xy9AkHwp8vSTJ04L0'
access_token_secret = 'A1cK98w2NXXaCWMqMW6p'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status('Hello Python Central!')

#ques4-->
API( is a part of library which defines how an application communicates with external code
API can be written in any language.
Library is written in same language which is a collection of all the functionalities required for the use case.
For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
For further reading : https://stackoverflow.com/questions/3678665/is-there-still-a-difference-between-a-library-
We can create our own APIs using Python Framework like Django and Flask which can be used in websites.
You can follow documentation of Django in order to create your own website with Python. Check this out:
https://docs.djangoproject.com/en/2.0/

'''
