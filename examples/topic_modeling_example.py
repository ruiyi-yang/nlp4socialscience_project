# Topic Modeling Example

from nlp4socialscience.topic_modeling import lda_topic_model

## define a corpus of documents
corpus = [
    "Politics and elections shape our daily lives.",
    "The economy plays a critical role in governance.",
    "Technological advances drive innovation.",
    "Sports can unify communities.",
    "Social media affects mental health and politics."
]

## perform LDA topic modeling with 2 topics
topics = lda_topic_model(corpus, num_topics=2)

for topic_id, words in topics.items():
    print(f"Topic {topic_id}: {[word for word, prob in words]}")