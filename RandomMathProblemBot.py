
'''
RANDOM MATH PROBLEM BOT
Jeff Thompson | 2013 | www.jeffreythompson.org

Some sample code for a tutorial on creating Twitter bots:
+ http://www.jeffreythompson.org/blog/2013/12/02/tutorial-twitter-bots

Requires the Python Twitter library:
+ https://github.com/bear/python-twitter

Questions or suggestions? Post them to the tutorial comments?

'''

from random import randrange							# random number generator
from OAuthSettings import settings				# load OAuth settings from separate file
import twitter														# load Twitter library

# load OAuth settings from separate file
consumer_key = settings['consumer_key']
consumer_secret = settings['consumer_secret']
access_token_key = settings['access_token_key']
access_token_secret = settings['access_token_secret']

# create two random numbers between -100/100
num1 = str(randrange(-100,100))
num2 = str(randrange(0,100))

# choose a random operator
operator = randrange(0,4)
if operator == 0:
	operator = '+'
elif operator == 1:
	operator = '-'
elif operator == 2:
	operator = '*'
elif operator == 3:
	operator = '/'

# computer the result using eval(), convert to a string
result = str(eval(num1 + operator + num2))

# format the Tweet nicely with spaces
tweet = num1 + ' ' + operator + ' ' + num2 + ' = ' + result
print tweet

# connect to Twitter and post
try:
	api = twitter.Api(
	consumer_key = consumer_key, 
	consumer_secret = consumer_secret, 
	access_token_key = access_token_key, 
	access_token_secret = access_token_secret)
	
	status = api.PostUpdate(tweet)				# this does the actual posting!
	print 'post successful!'

# catch any errors in posting
except twitter.TwitterError:
	print 'error posting!'

# all done! if running automatically, you may want to include the following line
# exit()
