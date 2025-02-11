# Test cases for topic_modeling 

import unittest
from nlp4socialscience.topic_modeling import lda_topic_model

class TestTopicModeling(unittest.TestCase):

    def test_lda_topic_model(self):
        corpus = [
            "Politics influences governance.",
            "Technology is evolving rapidly.",
            "Sports bring unity."
        ]
        result = lda_topic_model(corpus, num_topics=2)
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(len(result), 2)

if __name__ == "__main__":
    unittest.main()