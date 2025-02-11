# Quickstart Guide

Follow this guide to get started quickly with `nlp4socialscience`.

### Import the package
```python
from nlp4socialscience.preprocessing import clean_text
from nlp4socialscience.sentiment import sentiment_score
```

### Clean your text data

```python
text = "This is an amazing NLP package for social scientists!"
cleaned_text = clean_text(text)
print(cleaned_text)
```

### Analyze sentiment

```python
sentiment = sentiment_score(cleaned_text)
print(sentiment)
```

With these steps, you can preprocess text and perform sentiment analysis.