#!/usr/bin/env python
# coding: utf-8

#pip install tweepy

import tweepy

# Twitter Developer keys here
# It is CENSORED
consumer_key = 'xxxx'
consumer_key_secret = 'xxxx'
access_token = 'xxxx'
access_token_secret = 'xxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# This method creates the training set
def createTrainingSet(corpusFile, targetResultFile):
    import csv
    import time

    counter = 0
    corpus = []

    with open(corpusFile, 'r') as csvfile:
        lineReader = csv.reader(csvfile, delimiter=',', quotechar="\"")
        for row in lineReader:
            corpus.append({"tweet_id": row[1]})

    sleepTime = 2
    trainingDataSet = []

    for tweet in corpus:
        try:
            tweetFetched = api.get_status(tweet["tweet_id"],tweet_mode="extended")
            
            tweet["text"]=tweetFetched.full_text
            tweet["retweet_count"] = tweetFetched.retweet_count
            tweet["favorite_count"] = tweetFetched.favorite_count
            tweet["created"] = tweetFetched.created_at
            print(tweet["created"])
            tweet["userid"] = tweetFetched.user.id
            print(tweet["userid"])
            tweet["Geo"] = tweetFetched.geo
            tweet["Source"]=tweetFetched.source
            tweet["username"] = tweetFetched.user.screen_name
            print(tweet["username"])
            tweet["acctdesc"] = tweetFetched.user.description
            tweet["location"] = tweetFetched.user.location
            tweet["following"] = tweetFetched.user.friends_count
            tweet["followers"] = tweetFetched.user.followers_count
            tweet["totaltweets"] = tweetFetched.user.statuses_count
            tweet["usercreatedts"] = tweetFetched.user.created_at
            #tweet["hashtags"] = tweetFetchec.entities['hashtags']
            trainingDataSet.append(tweet)
            time.sleep(sleepTime)

        except:
            print("Inside the exception - no:2")
            continue

    with open(targetResultFile, 'w') as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',', quotechar="\"")
        for tweet in trainingDataSet:
            try:
                linewriter.writerow([tweet["tweet_id"],tweet["text"],tweet["retweet_count"],tweet["favorite_count"],
                                     tweet["created"], tweet["userid"],tweet["Geo"],tweet["Source"], tweet["username"],
                                    tweet["location"],tweet["following"],tweet["followers"],tweet["totaltweets"],
                                     tweet["acctdesc"],tweet["usercreatedts"]])
            except Exception as e:
                print(e)
    return trainingDataSet

# Code starts here
# This is corpus dataset
corpusFile = "inputdatasetfilename.csv"
# This is my target file
targetResultFile = "outputfilename.csv"
# Call the method
resultFile = createTrainingSet(corpusFile, targetResultFile)






