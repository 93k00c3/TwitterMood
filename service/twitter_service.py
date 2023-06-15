import nltk
from nltk.corpus import stopwords
import pandas as pd
import re
import langid


def filter_tweets(csv_file):
    df = pd.read_csv(csv_file)
    df['Tweet'] = df['Tweet'].apply(lambda x: re.sub(r'(@\w+)|(#\w+)|(http\S+|www\S+)|[^a-zA-Z0-9\s]', '', x.lower()))
    df = df[df['Tweet'].apply(lambda x: langid.classify(x)[0] == 'en')]
    df.dropna(subset=['Tweet'], inplace=True)
    return df['Tweet']


def preprocess_tweet(Tweet):
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    Tweet = re.sub(r'[^a-zA-Z\s]', '', Tweet)  # Remove special characters
    tweet_tokens = nltk.word_tokenize(Tweet)
    filtered_tokens = [word for word in tweet_tokens if word.lower() not in stop_words]  # Remove stopwords
    filtered_tweet = ' '.join(filtered_tokens)
    return filtered_tweet

