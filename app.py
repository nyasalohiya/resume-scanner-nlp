import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from utils.text_extraction import extract_text_from_file
from utils.preprocessing import preprocess_text
from utils.similarity import rank_resumes_by_similarity, get_top_keywords_for_text

st.set_page_config(page_title="Resume Scanner & Ranker", layout="wide")

st.title("Resume Scanner & Ranker — NLP-powered")
st.markdown("Upload resumes (PDF/DOCX/TXT) and a job description. The app ranks resumes by similarity to the job description.")

with st.sidebar:
    st.header("Upload")
    uploaded_files = st.file_uploader("Upload resumes (multiple)", type=["pdf","docx","txt"], accept_multiple_files=True)
    jd_text_input = st.text_area("Paste Job Description (or upload as .txt)", height=250)
    jd_file = st.file_uploader("Optional: Upload job description (.txt)", type=["txt"])
    method = st.selectbox("Vectorization method", ["tfidf", "spacy_embeddings"])
    top_k = st.number_input("Show top K resumes", min_value=1, max_value=50, value=5)
    run_button = st.button("Run")

# If user uploaded JD file, override text area
if jd_file is not None:
    jd_text_input = jd_file.read().decode("utf-8", errors="ignore")

if run_button:
    if len(uploaded_files) == 0:
        st.error("Please upload at least one resume file.")
    elif not jd_text_input.strip():
        st.error("Please paste or upload a job description.")
    else:
        # Extract and preprocess
        resumes = []
        for f in uploaded_files:
            raw = extract_text_from_file(f)
            resumes.append({"filename": f.name, "raw_text": raw})

        jd_raw = jd_text_input

        # Preprocess
        for r in resumes:
            r["clean_text"] = preprocess_text(r["raw_text"])
        jd_clean = preprocess_text(jd_raw)

        # Rank using similarity
        scores_df, vectorizer = rank_resumes_by_similarity([r["clean_text"] for r in resumes], jd_clean, method=method, filenames=[r["filename"] for r in resumes])

        # Display results
        st.subheader("Ranked Resumes")
        st.dataframe(scores_df)

        # Bar chart of top k
        st.subheader(f"Top {top_k} resumes (by similarity)")
        top_df = scores_df.head(int(top_k))
        st.bar_chart(top_df.set_index('filename')['similarity_score'])

        # Show matched keywords (TF-IDF based — fallback if vectorizer available)
        if vectorizer is not None and hasattr(vectorizer, 'get_feature_names_out'):
            st.subheader("Top matching keywords per top resume")
            jd_keywords = get_top_keywords_for_text(jd_clean, vectorizer, topn=20)
            st.success("Done — check the ranked results and download the CSV if needed.")
