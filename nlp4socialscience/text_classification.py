def classify_text(text: str, model='naive_bayes') -> str:
    """Classifies input text based on the chosen classifier."""
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.naive_bayes import MultinomialNB

    ## placeholder training corpus and labels
    corpus = ["Politics and government", "Sports and fitness", "Technology and science"]
    labels = ["Politics", "Sports", "Technology"]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    clf = MultinomialNB().fit(X, labels)

    ## predict label
    text_vector = vectorizer.transform([text])
    return clf.predict(text_vector)[0]
