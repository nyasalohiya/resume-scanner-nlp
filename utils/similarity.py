from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

def rank_resumes_by_similarity(resume_texts, jd_text, method='tfidf', filenames=None):
    """Returns a DataFrame with filenames and similarity scores in descending order.
    method: 'tfidf' or 'spacy_embeddings' (tfidf implemented here)."""
    if filenames is None:
        filenames = [f'resume_{i+1}' for i in range(len(resume_texts))]
    
    # combine resumes and JD for vectorization
    all_texts = resume_texts + [jd_text]

    if method == 'tfidf':
        vectorizer = TfidfVectorizer(max_features=20000, ngram_range=(1,2))
        X = vectorizer.fit_transform(all_texts)
        resume_vecs = X[:-1]
        jd_vec = X[-1]
        sims = cosine_similarity(resume_vecs, jd_vec.reshape(1, -1)).flatten()
    else:
        # fallback: simple TFIDF as above
        vectorizer = TfidfVectorizer(max_features=20000, ngram_range=(1,2))
        X = vectorizer.fit_transform(all_texts)
        resume_vecs = X[:-1]
        jd_vec = X[-1]
        sims = cosine_similarity(resume_vecs, jd_vec.reshape(1, -1)).flatten()

    df = pd.DataFrame({
        'filename': filenames,
        'similarity_score': sims
    })
    df = df.sort_values(by='similarity_score', ascending=False).reset_index(drop=True)
    return df, vectorizer

def get_top_keywords_for_text(text, vectorizer, topn=10):
    """Return topn keywords from the text using feature weights in TF-IDF vectorizer.
    Note: this function expects the vectorizer to have been fitted on corpus that includes this text."""
    try:
        features = vectorizer.get_feature_names_out()
    except Exception:
        features = vectorizer.get_feature_names()

    vec = vectorizer.transform([text])
    arr = vec.toarray().flatten()
    if arr.sum() == 0:
        return []
    idx = arr.argsort()[::-1][:topn]
    return [features[i] for i in idx if arr[i] > 0]
