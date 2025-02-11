# Basic Workflow Example for nlp4socialscience Package

### Install the package

``` bash
pip install nlp4socialscience
```



### Import the modules

```python
from nlp4socialscience.preprocessing import clean_text
from nlp4socialscience.sentiment import sentiment_score
from nlp4socialscience.topic_modeling import lda_topic_model
```



###  Clean and tokenize text

```python
text = "Natural Language Processing is crucial for modern social sciences."
cleaned = clean_text(text)
print("Cleaned Text:", cleaned)
```



### Analyze Sentiment

```python
sentiment = sentiment_score(cleaned)
print("Sentiment Analysis:", sentiment)
```



### Topic Modeling on a small corpus

```python
corpus = ["The economy impacts politics.", "Technological advances are key."]
topics = lda_topic_model(corpus, num_topics=2)
print("Topics:", topics)
```

 