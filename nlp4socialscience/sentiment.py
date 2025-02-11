def sentiment_score(text: str, model='vader') -> dict:
    """Returns sentiment scores (positive, neutral, negative)."""
    from nltk.sentiment import SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)