import csv
import re
from textblob import TextBlob


class Tweet:
    def __init__(self, full_text):
        self.full_text = full_text


with open('./archive/trumptweets.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        tweet_text = row['content']
        tweet_text_without_links = re.sub(r'http\S+', '', tweet_text)
        tweet = Tweet(tweet_text_without_links)
        analysis = TextBlob(tweet.full_text)
        print(analysis.sentiment)
