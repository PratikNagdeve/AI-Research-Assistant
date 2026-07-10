from collections import defaultdict

from utils.chatbot import get_llm


def compare_papers(chunks):
    """
    Compare all uploaded research papers.
    Uses hierarchical summarization:
    1. Group chunks by paper
    2. Create one summary per paper
    3. Compare summaries
    """

    llm = get_llm()

    # --------------------------------------------------
    # Group chunks by paper
    # --------------------------------------------------

    papers = defaultdict(list)

    for chunk in chunks:
        papers[chunk["source"]].append(chunk["text"])

    # --------------------------------------------------
    # Summarize each paper
    # --------------------------------------------------

    paper_summaries = []

    for paper_name, paper_chunks in papers.items():

        paper_text = "\n\n".join(paper_chunks[:15])  # Prevent huge prompts

        summary_prompt = f"""
You are an expert research scientist.

Read the research paper below and produce a concise structured summary.

Paper:
{paper_name}

Content:
----------------------
{paper_text}

Return ONLY the following sections.

## Research Problem

## Objective

## Methodology

## Dataset

## Model / Algorithm

## Results

## Strengths

## Limitations

## Future Work
"""

        summary = llm.invoke(summary_prompt).content

        paper_summaries.append(
            f"""
=========================
Paper: {paper_name}
=========================

{summary}
"""
        )

    # --------------------------------------------------
    # Final Comparison
    # --------------------------------------------------

    combined_summary = "\n\n".join(paper_summaries)

    comparison_prompt = f"""
You are an experienced AI researcher.

You have been provided summaries of multiple research papers.

Compare them professionally.

Paper Summaries
--------------------
{combined_summary}

Generate the comparison using the following format.

# 📊 Comparison Table

| Aspect | Paper 1 | Paper 2 | Paper 3 |
|--------|---------|---------|---------|
| Research Problem | | | |
| Objective | | | |
| Methodology | | | |
| Dataset | | | |
| Model | | | |
| Results | | | |
| Strengths | | | |
| Limitations | | | |

# 🔍 Comparative Analysis

Discuss similarities and differences.

# 💡 Key Insights

Mention important observations.

# 🚀 Research Gaps

Identify gaps across all papers.

# 📈 Future Research Directions

Suggest future work.

# ✅ Conclusion

Summarize the overall comparison.
"""

    comparison = llm.invoke(comparison_prompt)

    return comparison.content