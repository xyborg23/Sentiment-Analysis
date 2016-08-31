from textblob import TextBlob
import json
import re
import time


tweets = []
overall_sentiment = 0.0

for line in open('Tweets2.txt'):
    try:
        tweets.append(json.loads(line))
    except:
        pass

write_file = open("Tweets2_clean.txt", 'w')
write_file2 = open("tweet_sentiment_textblob.txt", 'w')

texts = [tweet['text'] for tweet in tweets]

start_time = time.time()
for text in texts:
    encoded_text = text.encode('utf-8')
    encoded_text = re.sub(r"(?:\@|https?\://)\S+", "", encoded_text)
    encoded_text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",encoded_text).split())
    encoded_text = encoded_text.replace("RT", "")
    encoded_text = encoded_text.strip()
    testimonial = TextBlob(encoded_text)
    print encoded_text
    print testimonial.sentiment
    write_file.write(encoded_text+"\n")
    write_file2.write(str(testimonial.sentiment.polarity))
    overall_sentiment = overall_sentiment + testimonial.sentiment.polarity
    write_file2.write("\n")

print("--- %s seconds ---" % (time.time() - start_time))
print "Overall sentiment", (overall_sentiment/len(texts))
write_file.close()
write_file2.close()