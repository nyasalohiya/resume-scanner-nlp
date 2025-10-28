# Detailed Setup Guide

## Windows Setup

### 1. Install Python
- Download Python 3.10+ from https://www.python.org/downloads/
- During installation, **check "Add Python to PATH"**
- Click Install

### 2. Install Git
- Download from https://git-scm.com/download/win
- Use default installation settings

### 3. Clone Repository
\`\`\`bash
git clone https://github.com/nyasalohiya/resume-scanner-nlp.git
cd resume-scanner-nlp
\`\`\`

### 4. Create Virtual Environment
\`\`\`bash
python -m venv venv
venv\Scripts\activate
\`\`\`

### 5. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 6. Download NLTK Data
\`\`\`bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('averaged_perceptron_tagger')"
\`\`\`

### 7. Run Application
\`\`\`bash
streamlit run app.py
\`\`\`

---

## macOS/Linux Setup

### 1. Install Python (if not installed)
\`\`\`bash
# macOS with Homebrew
brew install python3

# Ubuntu/Debian
sudo apt-get install python3 python3-pip
\`\`\`

### 2. Install Git (if not installed)
\`\`\`bash
# macOS
brew install git

# Ubuntu/Debian
sudo apt-get install git
\`\`\`

### 3. Clone Repository
\`\`\`bash
git clone https://github.com/YOUR_USERNAME/resume-scanner-nlp.git
cd resume-scanner-nlp
\`\`\`

### 4. Create Virtual Environment
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

### 5. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 6. Download NLTK Data
\`\`\`bash
python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('averaged_perceptron_tagger')"
\`\`\`

### 7. Run Application
\`\`\`bash
streamlit run app.py
\`\`\`

---

## Troubleshooting

### Python not found
- Make sure Python is added to PATH
- Try `python3` instead of `python`

### Permission denied on venv activation
\`\`\`bash
chmod +x venv/bin/activate
source venv/bin/activate
\`\`\`

### Port 8501 already in use
\`\`\`bash
streamlit run app.py --server.port 8502
\`\`\`

### NLTK data download fails
\`\`\`bash
# Try downloading individually
python -c "import nltk; nltk.download('stopwords')"
python -c "import nltk; nltk.download('wordnet')"
python -c "import nltk; nltk.download('averaged_perceptron_tagger')"
