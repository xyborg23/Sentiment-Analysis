from __future__ import division
import csv
from string import punctuation
import time


overall_sentiment = 0.0

tweets = open("Tweets2_clean.txt").read()
tweets_list = tweets.split('\n')

pos_sent = open("positive.txt").read()
positive_words=pos_sent.split('\n')
positive_counts=[]

neg_sent = open('negative.txt').read()
negative_words=neg_sent.split('\n')
negative_counts=[]

write_file = open("tweet_sentiment_basic.txt", 'w')

start_time = time.time()
for tweet in tweets_list:
    positive_counter=0
    negative_counter=0

    tweet_processed=tweet.lower()


    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')

    words=tweet_processed.split(' ')
    word_count=len(words)
    for word in words:
        if word in positive_words:
            positive_counter=positive_counter+1
        elif word in negative_words:
            negative_counter=negative_counter+1

    pos_val = positive_counter/word_count
    neg_val = negative_counter/word_count
    positive_counts.append(pos_val)
    negative_counts.append(neg_val)
    overall_sentiment = overall_sentiment + (pos_val - neg_val)
    write_file.write(str(pos_val-neg_val))
    write_file.write("\n")

print("--- %s seconds ---" % (time.time() - start_time))

print len(positive_counts)
print "Overall sentiment: ", overall_sentiment/len(positive_counts)

output=zip(tweets_list,positive_counts,negative_counts)

writer = csv.writer(open('tweet_sentiment.csv', 'wb'))
writer.writerows(output)

write_file.close()