# API Reference

Detailed documentation for key functions in the `nlp4socialscience` package.

### Preprocessing Module

**`clean_text(text: str, language='english') -> str`**

- Cleans input text by removing stopwords and punctuation.
- Example:
  ```python
  clean_text("This is a sample text with stopwords.")
  ```



### Sentiment Analysis Module

**`sentiment_score(text: str, model='vader') -> dict`**

- Returns sentiment scores (positive, neutral, negative).
- Example:
  ```python
  sentiment_score("I am happy with the product.")
  ```



### Topic Modeling Module

**`lda_topic_model(corpus: list, num_topics: int = 5) -> dict`**

- Performs topic modeling using Latent Dirichlet Allocation (LDA).
- Example:
  ```python
  lda_topic_model(["Text about politics.", "Economics topic."])
  ```