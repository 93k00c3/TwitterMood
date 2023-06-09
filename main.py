import pandas as pd
import re

df = pd.read_csv('./archive/NFT.csv')

tweets = df['tweets'].apply(lambda x: re.sub(r'(@\w+)|(#\w+)|(http\S+|www\S+)|[^a-zA-Z0-9\s]', '', x.lower()))
# Remove extra spaces
for tweet in tweets:
    print(tweet)
