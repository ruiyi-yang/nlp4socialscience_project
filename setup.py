from setuptools import setup, find_packages

setup(
    name='nlp4socialscience',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'nltk',
        'spacy',
        'gensim',
        'matplotlib',
        'wordcloud',
    ],
    description='An NLP package for social scientists to analyze text data easily',
    author='[Your Name]',
    author_email='[Your Email]',
    url='[Your Repo URL]',
)