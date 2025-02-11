# Sentiment Analysis Example

from nlp4socialscience.sentiment import sentiment_score

## analyze the sentiment of a given text
text = "The recent policy change is fantastic and beneficial to everyone."
result = sentiment_score(text)
 
print("Positive Sentiment:", result['pos'])
print("Neutral Sentiment:", result['neu'])
print("Negative Sentiment:", result['neg'])
print("Overall Sentiment Compound Score:", result['compound'])