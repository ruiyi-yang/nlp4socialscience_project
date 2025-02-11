def extract_entities(text: str, model='spacy') -> dict:
    """Extracts entities and categorizes them."""
    import spacy
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    return {ent.text: ent.label_ for ent in doc.ents}
