def lda_topic_model(corpus: list, num_topics: int = 5) -> dict:
    """Generates topics and returns keywords for each topic."""
    from gensim.corpora import Dictionary
    from gensim.models.ldamodel import LdaModel
 
    dictionary = Dictionary([doc.split() for doc in corpus])
    bow_corpus = [dictionary.doc2bow(doc.split()) for doc in corpus]

    ## train LDA model
    lda = LdaModel(corpus=bow_corpus, id2word=dictionary, num_topics=num_topics)

    ## extract topics and their words
    topics = {i: lda.show_topic(i) for i in range(num_topics)}
    return topics