#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Variables that contains the user credentials to access Twitter API
access_token = "2785418706-ZXbvoWpaoMykWZLZrnKcFSE719EnVdIivkDSXgi"
access_token_secret = "qsiSnfCtGYBA5vMtdX9BR5ZrqUNgFhDDNR3cTWncxl2z3"
consumer_key = "BM383gx41wFGV9Kr6dgtf2Wqy"
consumer_secret = "wjh95QfqOwZA9VLElyph9REC3HMf8eaweH4CEd5FduLfVFm8VZ"


# This is a basic listener that writes to a file.
class StdOutListener(StreamListener):

    def on_data(self, data):
        tweet = json.loads(data)
        encoded_tweet = tweet['text'].encode('ascii', 'ignore')
        print encoded_tweet
        target.write(data)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    target = open("Tweets2.txt", 'w')

    # This line filter Twitter Streams to capture data by the keywords
    stream.filter(languages=["en"], track=['donald trump', 'obama', 'hilary clinton'])

    target.close()