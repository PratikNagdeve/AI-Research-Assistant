import streamlit as st

from utils.pdf_loader import extract_text_from_pdf
from utils.text_splitter import split_documents
from utils.vectorstore import create_vectorstore
from utils.rag import answer_question
from utils.literature_review import generate_literature_review
from utils.paper_comparision import compare_papers


# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚",
    layout="wide",
)

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("📚 AI Research")

    st.markdown(
        """
Upload one or more research papers.

### Features

- 📄 Multi PDF Upload
- 🔍 Semantic Search
- 🤖 AI Question Answering
- 📖 Literature Review Generation
- 📊 Paper Comparison
- 📚 Source Citations
- 🧠 RAG Pipeline
"""
    )

    uploaded_files = st.file_uploader(
        "Upload PDFs",
        type=["pdf"],
        accept_multiple_files=True,
    )

    st.divider()

    if uploaded_files:

        st.subheader("Uploaded Papers")

        for file in uploaded_files:
            st.success(file.name)

# ---------------- Header ---------------- #

st.title("📚 AI Research Paper Assistant")

st.caption(
    "Chat with research papers using Retrieval-Augmented Generation (RAG), FAISS, LangChain and Gemini."
)

# ---------------- Empty State ---------------- #

if not uploaded_files:

    st.info(
        """
👈 Upload one or more research papers from the sidebar to begin.

Once uploaded you can:

• Ask questions

• Retrieve relevant passages

• View page citations

• Generate AI-powered answers

• Generate Literature Reviews

• Compare Research Papers
"""
    )

    st.stop()

# ---------------- Extract PDFs ---------------- #

all_pages = []

for file in uploaded_files:

    pages = extract_text_from_pdf(file)
    all_pages.extend(pages)

# ---------------- Chunking ---------------- #

chunks = split_documents(all_pages)

# ---------------- Vector Store ---------------- #

vectorstore = create_vectorstore(chunks)

# ---------------- Metrics ---------------- #

col1, col2, col3 = st.columns(3)

col1.metric("📄 Papers", len(uploaded_files))
col2.metric("📑 Pages", len(all_pages))
col3.metric("🧩 Chunks", len(chunks))

st.divider()

# ====================================================
# Tabs
# ====================================================

tab1, tab2, tab3 = st.tabs(
    [
        "💬 Chat",
        "📖 Literature Review",
        "📊 Paper Comparison",
    ]
)

# ====================================================
# Chat Tab
# ====================================================

with tab1:

    st.subheader("💬 Chat with your Papers")

    query = st.chat_input(
        "Ask a question about the uploaded papers..."
    )

    if query:

        with st.chat_message("user"):
            st.write(query)

        with st.spinner("🔍 Searching research papers..."):

            answer, docs = answer_question(
                vectorstore,
                query,
            )

        with st.chat_message("assistant"):

            st.markdown(answer)

        st.divider()

        st.subheader("📚 Retrieved Sources")

        for i, doc in enumerate(docs, start=1):

            with st.container(border=True):

                st.markdown(
                    f"""
### 📄 {doc.metadata['source']}

**Page:** {doc.metadata['page']}
"""
                )

                st.write(doc.page_content)

# ====================================================
# Literature Review Tab
# ====================================================

with tab2:

    st.subheader("📖 AI Literature Review")

    st.write(
        """
Generate a structured literature review from all uploaded research papers.

The generated review includes:

- Introduction
- Research Objectives
- Methodologies
- Datasets
- Key Findings
- Limitations
- Research Gaps
- Future Directions
- Conclusion
"""
    )

    if st.button(
        "📝 Generate Literature Review",
        use_container_width=True,
    ):

        with st.spinner(
            "Generating literature review..."
        ):

            review = generate_literature_review(
                chunks
            )

        st.success(
            "✅ Literature Review Generated Successfully!"
        )

        st.markdown(review)

# ====================================================
# Paper Comparison Tab
# ====================================================

with tab3:

    st.subheader("📊 AI Paper Comparison")

    st.write(
        """
Compare all uploaded research papers using AI.

The generated comparison includes:

- Research Problem
- Objectives
- Methodology
- Dataset
- Results
- Strengths
- Limitations
- Future Work
- Comparative Analysis
- Research Gaps
"""
    )

    st.info(
        f"Currently uploaded papers: **{len(uploaded_files)}**"
    )

    if len(uploaded_files) < 2:

        st.warning(
            "Please upload at least **2 research papers** to compare."
        )

    else:

        if st.button(
            "📊 Compare Papers",
            use_container_width=True,
            type="primary",
        ):

            with st.spinner(
                "Comparing research papers..."
            ):

                comparison = compare_papers(chunks)

            st.success(
                "✅ Paper Comparison Generated Successfully!"
            )

            st.markdown(comparison)

# ====================================================
# Expandable Chunks
# ====================================================

with st.expander("📚 View Generated Chunks"):

    st.write(f"Total Chunks: **{len(chunks)}**")

    for i, chunk in enumerate(chunks):

        with st.expander(
            f"Chunk {i+1} | {chunk['source']} | Page {chunk['page']}"
        ):

            st.write(chunk["text"])