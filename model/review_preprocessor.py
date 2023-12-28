import re

import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords  # noqa

english_stopwords = '|'.join(stopwords.words('english'))

regexes = {
    'HTML_TAG': re.compile(r'<([^>]+)>'),
    'PUNCTUATION': re.compile(r'[^a-z ]'),
    'SINGLE_CHARACTER': re.compile(r'\s+([a-z])\s+'),
    'SPACES': re.compile(r'\s+'),
    'STOPWORDS': re.compile(rf'\b({english_stopwords})\b'),
}


def preprocess_text(sentence: str) -> str:
    # lowercase everything
    sentence = sentence.lower()

    # remove html tags
    sentence = regexes['HTML_TAG'].sub('', sentence)

    # remove punctuations and numbers
    sentence = regexes['PUNCTUATION'].sub('', sentence)

    # remove single characters
    sentence = regexes['SINGLE_CHARACTER'].sub(' ', sentence)

    # remove stopwords
    sentence = regexes['STOPWORDS'].sub('', sentence)

    # remove additional spaces
    sentence = regexes['SPACES'].sub(' ', sentence)

    return sentence.strip(' ')
