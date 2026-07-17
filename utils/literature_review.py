from collections import defaultdict

from utils.chatbot import invoke_llm


def generate_literature_review(chunks):
    """
    Generate a literature review from multiple papers while
    keeping the prompt size manageable for Gemini Flash.
    """

    # -------------------------------
    # Group chunks by paper
    # -------------------------------

    papers = defaultdict(list)

    for chunk in chunks:
        papers[chunk["source"]].append(chunk)

    # -------------------------------
    # Build context
    # -------------------------------

    context = ""

    MAX_CHUNKS_PER_PAPER = 5
    MAX_CONTEXT_LENGTH = 25000

    for paper_name, paper_chunks in papers.items():

        context += f"\n========== {paper_name} ==========\n\n"

        for chunk in paper_chunks[:MAX_CHUNKS_PER_PAPER]:

            context += f"""
Page: {chunk['page']}

{chunk['text']}

------------------------------------------
"""

            if len(context) >= MAX_CONTEXT_LENGTH:
                break

        if len(context) >= MAX_CONTEXT_LENGTH:
            break

    print(f"Literature Review Prompt Length: {len(context)} characters")

    # -------------------------------
    # Prompt
    # -------------------------------

    prompt = f"""
You are an expert research assistant and academic writer.

You have been provided with excerpts from one or more research papers.

Generate a professional literature review.

Rules:
- Use ONLY the provided context.
- Do NOT invent information.
- If information is unavailable, simply omit it.
- Synthesize ideas across papers instead of describing papers one by one.
- Write in an academic style.

Structure your response as follows:

# Introduction

# Research Objectives

# Methodologies

# Datasets

# Key Findings

# Limitations

# Research Gaps

# Future Directions

# Conclusion

Context
-------

{context}
"""

    literature_review = invoke_llm(prompt)

    return literature_review