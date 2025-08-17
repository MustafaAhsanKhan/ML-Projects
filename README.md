# ML Projects Monorepo

Lightweight machine learning / AI demo collection. Each folder is an independent Python 3.13+ project (install with `uv pip install .` or standard tooling).

---

## Projects

### 1. AI Educational Agent
Streaming CLI ReAct agent limited to education/study‑abroad queries (LangChain + LangGraph + OpenRouter).  
Docs: [AI-Agent/README.md](AI-Agent/README.md)

### 2. Fake News Detection System
TF‑IDF + Logistic Regression on LIAR dataset with metrics & ROC utilities.  
Docs: (pending) Folder: [Fake-News-Detection-System](Fake-News-Detection-System)

### 3. Image Classifier
Streamlit MobileNetV2 (ImageNet) app returning top‑3 labels with caching.  
Docs: (pending) Folder: [Image-Classifier](Image-Classifier)

### 4. Memory Based Chatbot
Streaming ReAct conversational helper with buffer memory for context retention.  
Docs: (pending) Folder: [Memory-Based-Chatbot](Memory-Based-Chatbot)

### 5. Named Entity Recognition (NER) System
spaCy inference helper exposing entity span extraction via `en_core_web_sm`.  
Docs: (pending) Folder: [NER-System](NER-System)

### 6. Resume Critiquer
Streamlit tool parses PDF/TXT resumes and prompts an LLM for structured feedback.  
Docs: (pending) Folder: [Resume-Critiquer](Resume-Critiquer)

### 7. Rule Based Chatbot
Intent / pattern matcher using token overlap over JSON intents for educational Q&A.  
Docs: (pending) Folder: [Rule-Based-Chatbot](Rule-Based-Chatbot)

### 8. Text Summarization Tool
CLI LSA (Sumy) summarizer with light text preprocessing & NLTK stopwords.  
Docs: (pending) Folder: [Text-Summarization-Tool](Text-Summarization-Tool)

---

## Quick Start
1. cd <project-folder>
2. uv venv && (Windows) .venv\Scripts\activate  (Unix) source .venv/bin/activate
3. uv pip install .   (or: uv pip install -r requirements.txt)
4. python main.py   (or project-specific entry)