from service.twitter_service import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt



filtered_tweets = filter_tweets('./archive/worldcuptweets.csv')
filtered_tweets = filtered_tweets[filtered_tweets != '']
all_tweets = ' '.join(filtered_tweets)

wordcloud = WordCloud(width=800, height=400, background_color='white',
                      stopwords=None).generate(all_tweets)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

sentiments = []
for tweet in filtered_tweets:
    sentiment = analyze_sentiment(tweet)
    sentiments.append(sentiment)

sentiment_counts = {
    'Positive': sentiments.count('Positive'),
    'Negative': sentiments.count('Negative'),
    'Neutral': sentiments.count('Neutral')
}

labels = sentiment_counts.keys()
values = sentiment_counts.values()

plt.bar(labels, values)
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Sentiment Analysis of Tweets')
plt.show()
