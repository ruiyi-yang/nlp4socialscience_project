 # Test cases for preprocessing

import unittest
from nlp4socialscience.preprocessing import clean_text, custom_tokenize 


class TestPreprocessing(unittest.TestCase):

    def test_clean_text(self):
        text = "This is a sample sentence with punctuation!"
        result = clean_text(text)
        self.assertTrue(isinstance(result, str))
        self.assertIn('punctuation', result)   
        self.assertNotIn('!', result)   

    def test_custom_tokenize(self):
        text = "Tokenize this sentence correctly."
        tokens = custom_tokenize(text)
        self.assertTrue(isinstance(tokens, list))
        self.assertEqual(len(tokens), 4)   

if __name__ == "__main__":
    unittest.main()
