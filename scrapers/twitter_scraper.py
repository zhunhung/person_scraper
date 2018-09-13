from twitter import *

import sys
sys.path.append(".")
import config_keys
import pandas as pd

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config_keys.access_key,
                  config_keys.access_secret,
                  config_keys.consumer_key,
                  config_keys.consumer_secret))

def checkTwitter(name, folder):
    query = twitter.search.tweets(q=name)
    created = []
    screen_name = []
    tweet = []
    for result in query["statuses"]:
        created.append(result["created_at"])
        screen_name.append(result["user"]["screen_name"])
        tweet.append(result["text"])
    result_df = pd.DataFrame({'Created At':created, 'User':screen_name,'Message':tweet})
    print("Found " + str(len(result_df)) + " matches in Twitter")
    fileName = folder + '/' + name.replace(' ', '_') + '_tweets.csv'
    result_df.to_csv(fileName, encoding='utf-8', header=True, index=False)