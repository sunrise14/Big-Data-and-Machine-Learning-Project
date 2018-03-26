from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'B6tZdUyY6vHnMWYW79J9sUZzS'
csecret = 'F6n10hAo2n8VQFSNQEXliLCNRxjtJwshInF6A95RbZoUViaYOA'
atoken = '787526326018117632-KlRhZDNMxddJQJsHvpDZYMmz5cUaJiX'
asecret = 'VBspTZpYNjQ7A1nxrZWB8Mp6rJCzBlUB7rPFismnmDzNK'

class listener(StreamListener):
    def on_data(self, data):
        try:
            print(data)
            saveFile = open("f:\\tweets.csv","a")
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return(True)
        except BaseException as e:
            print('failed ondata,',str(e))
            time.sleep(5)

def on_error(self, status):
    print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['Construction Worker','Helmet'])