# NLP4SocialScience

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Build](https://img.shields.io/badge/build-passing-brightgreen)



`nlp4socialscience` is a user-friendly Natural Language Processing (NLP) package specifically designed for social science researchers who want to explore and analyze textual data without needing extensive coding experience. The package provides ready-to-use tools for key NLP tasks, including text cleaning, sentiment evaluation, topic discovery, named entity identification, and trend detection. By streamlining these processes, `nlp4socialscience` empowers researchers to gain meaningful insights from text-based data efficiently.



### Key Features

- **Text Preprocessing**: Clean and tokenize raw text by removing stopwords, punctuation, and performing lemmatization.
- **Sentiment Analysis**: Automatically evaluate the sentiment of text using pre-trained models.
- **Topic Modeling**: Extract underlying topics from large collections of documents.
- **Named Entity Recognition (NER)**: Identify important entities, such as names, organizations, and locations.
- **Trend Analysis**: Track the frequency of terms over time for longitudinal studies.
- **Data Visualization**: Generate word clouds and other visual representations for better data comprehension.



### **Installation**

To install the package, run:
```bash
pip install nlp4socialscience
```

For detailed installation instructions, refer to the [Installation Guide](./docs/installation.md).

 

### **Quickstart Guide**

Follow these simple steps to get started:

1. Import the necessary modules:
    ```python
    from nlp4socialscience.preprocessing import clean_text
    from nlp4socialscience.sentiment import sentiment_score
    from nlp4socialscience.topic_modeling import lda_topic_model
    ```

2. Preprocess your text:
    ```python
    text = "This is an amazing NLP package for social scientists!"
    cleaned_text = clean_text(text)
    print("Cleaned Text:", cleaned_text)
    ```

3. Analyze sentiment:
    ```python
    sentiment = sentiment_score(cleaned_text)
    print("Sentiment Analysis:", sentiment)
    ```

For more detailed examples, check the [Quickstart Guide](./docs/quickstart.md).



### Example Usage

#### 1. Topic Modeling
```python
from nlp4socialscience.topic_modeling import lda_topic_model

corpus = [
    "Politics influences governance.",
    "Technology drives innovation.",
    "Economic policies affect growth.",
    "Sports unite communities."
]

topics = lda_topic_model(corpus, num_topics=2)
for topic_id, words in topics.items():
    print(f"Topic {topic_id}: {[word for word, prob in words]}")
```

#### 2. Sentiment Analysis
```python
from nlp4socialscience.sentiment import sentiment_score

text = "The policy changes have positively impacted many citizens."
result = sentiment_score(text)
print(result)
```



### API Reference

For a detailed overview of all available modules and functions, check the [API Reference](./docs/api_reference.md).



### Project Structure

```plaintext
nlp4socialscience/
├── nlp4socialscience/       # core modules for NLP tasks
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── sentiment.py
│   ├── topic_modeling.py
│   ├── named_entity_recognition.py
│   ├── text_classification.py
│   ├── trend_analysis.py
│   ├── utils.py
│   └── visualizations.py
├── examples/                # example scripts
├── docs/                    # documentation (Installation, API, FAQs)
├── tests/                   # unit tests
├── setup.py                 # installation script
├── README.md                # project description and usage guide
├── requirements.txt         # project dependencies
└── LICENSE                  # license information
```

#### **Core Modules**

| Module                        | Functionality                                      | Example Usage                       |
| ----------------------------- | -------------------------------------------------- | ----------------------------------- |
| `preprocessing.py`            | Text cleaning, tokenization, and lemmatization     | `clean_text()`, `custom_tokenize()` |
| `sentiment.py`                | Analyze text sentiment using built-in models       | `sentiment_score()`                 |
| `topic_modeling.py`           | Discover hidden topics in documents                | `lda_topic_model()`                 |
| `named_entity_recognition.py` | Extract named entities like names, organizations   | `extract_entities()`                |
| `trend_analysis.py`           | Identify and visualize term frequencies over time  | `term_frequency_over_time()`        |
| `visualizations.py`           | Generate word clouds and text-based visualizations | `plot_wordcloud()`                  |



### Dependencies

- `numpy`
- `pandas`
- `nltk`
- `spacy`
- `gensim`
- `scikit-learn`
- `matplotlib`
- `wordcloud`

All dependencies can be installed via the `requirements.txt` file:
```bash
pip install -r requirements.txt
```



### Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository on GitHub.
2. Create a new branch for your feature.
3. Submit a pull request.

For any issues, please open a ticket in the [GitHub Issues](https://github.com/ruiyi-yang/NLP4SocialScience/issues) section.



### FAQ

For frequently asked questions, visit the [FAQ Section](./docs/faq.md).

### License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

### Acknowledgments

Special thanks to the social science community and contributors who helped shape this package.
