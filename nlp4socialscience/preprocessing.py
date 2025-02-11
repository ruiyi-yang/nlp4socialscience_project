import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def custom_tokenize(text: str) -> list:
    """Tokenizes input text."""
    return text.split()

def clean_text(text: str, language='english') -> str:
    """Removes punctuation marks and stopwords, but keeps words like 'punctuation'."""
    stop_words = set(stopwords.words(language))
    lemmatizer = WordNetLemmatizer()

    ## remove punctuation marks using regex and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text.lower())

    ## tokenize, clean, and lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words]
    return ' '.join(tokens)

def test_clean_text(self):
    text = "This is a sample sentence with punctuation!"
    result = clean_text(text)
    self.assertTrue(isinstance(result, str))
    self.assertIn('punctuation', result)  ## the word should be retained

