import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet', quiet=True)

try:
    nltk.data.find('corpora/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger', quiet=True)

_lemmatizer = None
_stop_words = None

def get_lemmatizer():
    global _lemmatizer
    if _lemmatizer is None:
        _lemmatizer = WordNetLemmatizer()
    return _lemmatizer

def get_stop_words():
    global _stop_words
    if _stop_words is None:
        _stop_words = set(stopwords.words('english'))
    return _stop_words

def preprocess_text(text: str) -> str:
    """Lowercase, remove punctuation, digits, extra whitespace, stopwords, and lemmatize."""
    if not text:
        return ''
    
    # Quick clean
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    
    lemmatizer = get_lemmatizer()
    stop_words = get_stop_words()
    
    tokens = []
    words = text.split()
    
    for word in words:
        word = word.strip()
        if word and word not in stop_words and len(word) > 1:
            lemma = lemmatizer.lemmatize(word)
            tokens.append(lemma)
    
    return ' '.join(tokens)
