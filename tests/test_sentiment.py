# Test cases for sentiment 

import unittest
from nlp4socialscience.sentiment import sentiment_score

class TestSentiment(unittest.TestCase):

    def test_sentiment_positive(self):
        text = "I am very happy with the results!"
        result = sentiment_score(text)
        self.assertGreater(result['pos'], 0)
        self.assertGreater(result['compound'], 0)

    def test_sentiment_negative(self):
        text = "This is a terrible situation."
        result = sentiment_score(text)
        self.assertGreater(result['neg'], 0)
        self.assertLess(result['compound'], 0)

if __name__ == "__main__":
    unittest.main()