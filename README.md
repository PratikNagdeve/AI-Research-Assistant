# 📚 AI Research Paper Assistant

An AI-powered research assistant that enables users to interact with multiple research papers using **Retrieval-Augmented Generation (RAG)**. The application supports semantic search, question answering, literature review generation, and AI-powered comparison of research papers through an intuitive Streamlit interface.

---

## 🚀 Live Demo

**Live Application:** `https://ai-research-assistant-pratiknagdeve.streamlit.app/`

**GitHub Repository:** `https://github.com/PratikNagdeve/AI-Research-Assistant`

---

# 📖 Overview

Reading and comparing multiple research papers is a time-consuming process. This project simplifies academic literature exploration by allowing users to upload multiple PDF research papers and interact with them using natural language.

The system leverages transformer-based embeddings, a FAISS vector database, and Google's Gemini Large Language Model to retrieve relevant information and generate context-aware responses.

---

# ✨ Features

### 📄 Multi-PDF Upload

* Upload multiple research papers simultaneously.
* Supports PDF documents.
* Automatically extracts and processes text from uploaded papers.

### 🔍 Semantic Search

* Retrieves relevant content based on semantic similarity rather than keyword matching.
* Uses Sentence Transformers for embedding generation.
* Powered by FAISS for efficient vector search.

### 🤖 AI Question Answering

* Ask questions in natural language.
* Uses Retrieval-Augmented Generation (RAG).
* Generates answers grounded in the uploaded research papers.
* Displays retrieved source passages for transparency.

### 📖 Literature Review Generator

Automatically generates a structured literature review containing:

* Introduction
* Research Objectives
* Methodologies
* Datasets
* Key Findings
* Limitations
* Research Gaps
* Future Directions
* Conclusion

### 📊 AI Paper Comparison

Compare multiple research papers across:

* Research Problem
* Objectives
* Methodology
* Dataset
* Model/Algorithm
* Results
* Strengths
* Limitations
* Future Work

Also provides:

* Comparative Analysis
* Key Insights
* Research Gaps
* Future Research Directions
* Overall Conclusion

### 📚 Source Citations

* Displays retrieved document chunks.
* Shows page numbers for supporting evidence.
* Improves answer transparency.

---

# 🏗 System Architecture

```text
                 PDF Research Papers
                         │
                         ▼
                Text Extraction (PyMuPDF)
                         │
                         ▼
                 Document Chunking
                         │
                         ▼
       Sentence Transformer Embeddings
                         │
                         ▼
                FAISS Vector Database
                         │
                         ▼
             Semantic Similarity Search
                         │
                         ▼
                 Google Gemini LLM
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
 Question Answering  Literature Review  Paper Comparison
```

---

# 🛠 Tech Stack

### Programming Language

* Python

### Frontend

* Streamlit

### AI Framework

* LangChain

### Large Language Model

* Google Gemini

### Embedding Model

* Sentence Transformers

  * all-MiniLM-L6-v2

### Vector Database

* FAISS

### PDF Processing

* PyMuPDF

---

# 📂 Project Structure

```text
AI-Research-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── utils/
│   ├── chatbot.py
│   ├── literature_review.py
│   ├── paper_comparison.py
│   ├── pdf_loader.py
│   ├── rag.py
│   ├── text_splitter.py
│   └── vectorstore.py
│
└── assets/
    ├── screenshots/
    └── architecture.png
```

---

# ⚙ Installation

## Clone the repository

```bash
git clone https://github.com/PratikNagdeve/AI-Research-Assistant.git

cd AI-Research-Assistant
```

## Create a virtual environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Create a `.env` file

```text
GEMINI_API_KEY=your_google_gemini_api_key
```

## Run the application

```bash
streamlit run app.py
```

---

# 📸 Screenshots

Add screenshots after deployment.

Suggested screenshots:

* Home Page
* Chat Interface
* Literature Review Generation
* Paper Comparison
* Retrieved Sources

---

# 💡 Use Cases

* Academic research
* Literature survey
* Research paper exploration
* Comparative analysis of scientific papers
* Student projects
* Research assistance

---

# 🚀 Future Improvements

* PDF report export
* Chat history
* Persistent vector database
* Hybrid retrieval (semantic + keyword search)
* Research paper recommendation system
* Citation export
* User authentication
* Cloud storage support

---

# 📈 Skills Demonstrated

This project demonstrates practical experience with:

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Prompt Engineering
* Semantic Search
* Vector Databases (FAISS)
* Transformer Embeddings
* LangChain
* Information Retrieval
* Multi-document Question Answering
* AI-powered Literature Review Generation
* AI-based Paper Comparison
* Streamlit Application Development

---

# 👨‍💻 Author

**Pratik Nagdeve**

M.Tech in Artificial Intelligence

Maulana Azad National Institute of Technology (MANIT), Bhopal

GitHub: https://github.com/PratikNagdeve

---

# 📜 License

This project is released under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
