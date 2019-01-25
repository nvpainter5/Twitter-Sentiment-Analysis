from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mode as s
#from twitterapistuff import *

#consumer key, consumer secret, access token, access secret.
ckey="JYRJx37HW15lftfUNjJziMhrM"
csecret="YtDYHqSn43zt0FhBnJyPfbwDarlV6B0YRdtEI8KD18zTWe3CWB"
atoken="416194224-46878nz7kIimyjD5ywNTdyCXvHQyZ0AguDMeSZk5"
asecret="96cQ8trB4LUjyv21iHDokx7G4kTXX4KixYQfoixJe4uqM"

class listener(StreamListener):
    
    def on_data(self, data):
        
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value = s.sentiment(tweet)
        print(tweet, sentiment_value)
        
        output = open("twitter-out.txt","a")
        output.write(sentiment_value)
        output.write('\n')
        output.close()
		 
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])