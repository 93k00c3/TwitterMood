import pandas as pd
import re
import langid


def filter_tweets(csv_file):
    df = pd.read_csv(csv_file)
    df['Tweet'] = df['Tweet'].apply(lambda x: re.sub(r'(@\w+)|(#\w+)|(http\S+|www\S+)|[^a-zA-Z0-9\s]', '', x.lower()))
    df = df[df['Tweet'].apply(lambda x: langid.classify(x)[0] == 'en')]
    df.dropna(subset=['Tweet'], inplace=True)
    return df['Tweet']
