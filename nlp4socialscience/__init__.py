## initialization file for the nlp4socialscience package.
## imports core modules for users to access them easily.
 
from .preprocessing import clean_text, custom_tokenize
from .sentiment import sentiment_score
from .topic_modeling import lda_topic_model
from .named_entity_recognition import extract_entities
from .text_classification import classify_text
from .trend_analysis import term_frequency_over_time
from .utils import load_texts_from_csv
from .visualizations import plot_wordcloud

# __all__ lists accessible objects for wildcard imports
__all__ = [
    "clean_text", "custom_tokenize", "sentiment_score", "lda_topic_model", "extract_entities",
    "classify_text", "term_frequency_over_time", "load_texts_from_csv", "plot_wordcloud"
]
