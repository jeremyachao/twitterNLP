from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

ckey="VPwKRTOGDO2ZfWZBpaexKgmXx"
csecret="KVXafx8Y2MGoXba22pZlWTGrNyEP66FcZp3AE1rOXHQqMTHc42"
atoken="1097172671710875648-ggWCpbrldo32n2gw2pD8Bug9AK6dcx"
asecret="vo0ZOFBLqs9bqPvyRHCHtCsqGR5YqDuDET0s98U1EUKUD"

class listener(StreamListener):
    def on_data(self, data):
        try:
            all_data = json.loads(data)
            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)

            if confidence*100 >= 80:
            	output = open("twitter-out.txt","a")
            	output.write(sentiment_value)
            	output.write('\n')
            	output.close()

            return True
        except:
            return True


    def on_error(self, status):
        print('ERROR: '+ str(status))

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])
