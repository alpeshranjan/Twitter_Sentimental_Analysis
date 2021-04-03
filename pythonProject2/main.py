from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100 * float(part)/float(whole)

api_key = "4J57oirNVrtCoOKjDZjJ7JWNd"
api_secret = "W7G8RwtRXYTZyLaOeAhDV78AAF7bW1c55IdeqFrMinGOC2cyJu"
access_token = "771213632046641152-AqWFSaq6OLxJD2xu47ETuru3mSH6YWY"
access_token_secret = "9hDS9d77cnIYYZrykMQWxINDujHPOBy1Hgol2v45stOtz"

#establish the connection with twitter API in python code

auth = tweepy.OAuthHandler(api_key, api_secret)
#for saving accessToken and AccessTokenSecret
auth.set_access_token(access_token, access_token_secret)
#variable object created for the api we have to use
api = tweepy.API(auth) #successfully established the connection with API


searchword = input("enter the word : ")
noOfsearch = int(input("enter number of tweets to analyse : "))

#performing sentimental analysis
tweets = tweepy.Cursor(api.search, q=searchword, language="English").items(noOfsearch)

#initializing 0 so they do not take garbage value and this should be the average value for tweets

positive = 0
negative = 0
neutral = 0
polarity = 0 #polarity is average sentiment of all the tweets



for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    #pass the text of tweet for sentiment analysis and store it in polarity variable
    polarity += analysis.sentiment.polarity

    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1

#using %func created earlier to find percent and plot on the graph

positive = percentage(positive, noOfsearch)
negative = percentage(negative, noOfsearch)
neutral = percentage(neutral, noOfsearch)
polarity = percentage(polarity, noOfsearch)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

#printing the results

print("Sentimental Analysis of " + searchword + " by analyzing " + str(noOfsearch) + " Tweets.")

if (polarity == 0):
    print("Neutral")
elif(polarity < 0.00):
    print("Negative")
elif(polarity > 0.00):
    print("Positive")

#printing the pie-chart using matplotlib

labels = ['positive['+str(positive)+'%]'], ['negative['+str(negative)+'%]'], ['neutral['+str(neutral)+'%]']
sizes = [positive, neutral, negative]
colors = ['green', 'grey', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc ="best")
plt.title(("Sentimental Analysis of " + searchword + " by analyzing " + str(noOfsearch) + " Tweets."))
plt.axis('equal')
plt.tight_layout()
plt.show()
