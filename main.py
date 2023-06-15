from service.twitter_service import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt


filtered_tweets = filter_tweets('./archive/worldcuptweets.csv')
filtered_tweets = filtered_tweets[filtered_tweets != '']
all_tweets = ' '.join(filtered_tweets)

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_tweets)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()