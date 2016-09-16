#!/usr/bin/python3

# Accessing the Twitter API
# This script describes the basic methodology for accessing a Twitter feed
# or something similar.

# Loading libraries needed for authentication and requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import json

# In order to use this script, you must:
# - Have a Twitter account and create an app
# - Store in keys.json a property called "twitter" whose value is an
#     object with two keys, "key" and "secret"
with open('keys.json', 'r') as f:
   keys = json.loads(f.read())['twitter']

twitter_key = keys['key']
twitter_secret = keys['secret']

# We authenticate ourselves with the above credentials
# We will demystify this process later
#
# For documentation, see http://requests-oauthlib.readthedocs.io/en/latest/api.html
# and http://docs.python-requests.org/en/master/
client = BackendApplicationClient(client_id=twitter_key)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url='https://api.twitter.com/oauth2/token',
                          client_id=twitter_key,
                          client_secret=twitter_secret)

# Base url needed for all subsequent queries
base_url = 'https://api.twitter.com/1.1/'

# Particular page requested. The specific query string will be
# appended to that.
page = 'search/tweets.json'

# Depending on the query we are interested in, we append the necessary string
# As you read through the twitter API, you'll find more possibilities
req_url = base_url + page + '?q=from:realDonaldTrump&count=100'

# We perform a request. Contains standard HTTP information
response = oauth.get(req_url)

# Read the query results
results = json.loads(response.content.decode('utf-8'))

# Reads all tweets up to a limit (default 30000)
# and returns the array
# query should be the query string to be searched for (will go into the "?q=" part)
def getTweets(url, query, limit = 30000):
  initialQuery = url + '?q=' + query +'&count=100'
  response = oauth.get(initialQuery)
  results = json.loads(response.content.decode('utf-8'))
  tweets = results['statuses']
  while len(tweets) <= limit:
    if not ('next_results' in results['search_metadata']):
      break
    next_search = base_url + page + results['search_metadata']['next_results']
    response = oauth.get(next_search)
    results = json.loads(response.content.decode('utf-8'))
    tweets.extend(results['statuses'])
  return tweets

# We use the above function to get all tweets from the two presidential candidates.
hillary = getTweets(base_url+page, 'from:HillaryClinton')
donald = getTweets(base_url+page, 'from:realDonaldTrump')

## Insert answers to problems 1-6 here


## CAUTION: You should put your answers to problems 1-6 ABOVE this line
# The space below is for problems 7-9.
#
# An example request:
# oauth.get(base_url+'followers/ids.json?screen_name=HanoverCollege')
# This returns a "response" object, you can learn about those at:
# http://docs.python-requests.org/en/master/user/quickstart/#response-content
# This function is for question 7
def fetchFollowerIds(screen_name):
  [] # You will need to replace this

# This function is for question 8
def fetchUsers(ids):
  [] # You will need to replace this

# This function is for question 9, and should be quite short, using the previous 2
def getFollowers(screen_name):
  [] # You will need to replace this
