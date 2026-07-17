from collections import defaultdict

from utils.chatbot import invoke_llm


def compare_papers(chunks):
    """
    Compare uploaded research papers while keeping
    the prompt size small enough for Gemini Flash.
    """

    # ----------------------------------------
    # Group chunks by paper
    # ----------------------------------------

    papers = defaultdict(list)

    for chunk in chunks:
        papers[chunk["source"]].append(chunk)

    # ----------------------------------------
    # Build context
    # ----------------------------------------

    context = ""

    MAX_CHUNKS_PER_PAPER = 4
    MAX_CONTEXT_LENGTH = 25000

    for i, (paper_name, paper_chunks) in enumerate(papers.items(), start=1):

        context += f"\n===============================\n"
        context += f"Paper {i}: {paper_name}\n"
        context += f"===============================\n\n"

        for chunk in paper_chunks[:MAX_CHUNKS_PER_PAPER]:

            context += f"""
Page: {chunk['page']}

{chunk['text']}

----------------------------------------
"""

            if len(context) >= MAX_CONTEXT_LENGTH:
                break

        if len(context) >= MAX_CONTEXT_LENGTH:
            break

    print(f"Comparison Prompt Length: {len(context)} characters")

    # ----------------------------------------
    # Dynamic table
    # ----------------------------------------

    num_papers = len(papers)

    headers = " | ".join(
        [f"Paper {i}" for i in range(1, num_papers + 1)]
    )

    separator = " | ".join(["---"] * num_papers)

    # ----------------------------------------
    # Prompt
    # ----------------------------------------

    comparison_prompt = f"""
You are an experienced AI researcher.

Compare the following research papers.

Rules:

- Use ONLY the provided context.
- Do NOT invent information.
- If an aspect is missing, write "Not Mentioned".
- Keep each table cell concise (1-2 sentences).
- After the table, provide an analytical comparison.

Research Papers
---------------

{context}

Generate the response using exactly this structure.

# 📊 Comparison Table

| Aspect | {headers} |
|--------|{separator}| 
| Research Problem | |
| Objective | |
| Methodology | |
| Dataset | |
| Model / Algorithm | |
| Results | |
| Strengths | |
| Limitations | |

# 🔍 Comparative Analysis

Discuss:
- Similarities
- Differences
- Strengths of each approach
- Weaknesses of each approach

# 💡 Key Insights

Provide the major observations.

# 🚀 Research Gaps

Identify common research gaps.

# 📈 Future Research Directions

Suggest future research opportunities.

# ✅ Conclusion

Provide a concise conclusion.
"""

    comparison = invoke_llm(comparison_prompt)

    return comparison