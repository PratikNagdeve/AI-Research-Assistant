from utils.chatbot import get_llm


def generate_literature_review(chunks):

    context = ""

    for chunk in chunks:

        context += f"""
Paper: {chunk['source']}
Page: {chunk['page']}

{chunk['text']}

------------------------------------------
"""

    prompt = f"""
You are an expert research assistant and academic writer.

You have been provided with content extracted from one or more research papers.

Your task is to generate a professional literature review.

Use ONLY the provided context.

Do NOT invent information.

If multiple papers discuss similar ideas, synthesize them together instead of describing each paper separately.

Write the literature review using the following structure.

# Introduction

Briefly introduce the research area.

# Research Objectives

Summarize the objectives addressed by the papers.

# Methodologies

Discuss the methodologies and techniques used.

# Datasets

Describe the datasets used, if mentioned.

# Key Findings

Summarize the important findings.

# Limitations

Mention the limitations discussed.

# Research Gaps

Identify gaps that remain unsolved.

# Future Directions

Summarize future research suggested by the papers.

# Conclusion

Provide a concise conclusion.

Context:

{context}
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content