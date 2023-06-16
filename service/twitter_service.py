import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
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
    lemmatizer = WordNetLemmatizer()
    Tweet = re.sub(r'[^a-zA-Z\s]', '', Tweet)
    tweet_tokens = nltk.word_tokenize(Tweet)
    filtered_tokens = [lemmatizer.lemmatize(word) for word in tweet_tokens if word.lower() not in stop_words]
    filtered_tweet = ' '.join(filtered_tokens)
    return filtered_tweet


def analyze_sentiment(Tweet):
    blob = TextBlob(Tweet)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return 'Positive'
    elif sentiment < 0:
        return 'Negative'
    else:
        return 'Neutral'
