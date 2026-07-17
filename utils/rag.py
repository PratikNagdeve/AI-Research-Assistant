from utils.chatbot import invoke_llm


def answer_question(vectorstore, query):

    docs = vectorstore.similarity_search(query, k=3)

    context = ""

    for doc in docs:
        context += f"""
Source: {doc.metadata['source']}
Page: {doc.metadata['page']}

{doc.page_content}

----------------------------------------
"""

    prompt = f"""
You are an AI Research Assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, reply exactly:

"I could not find the answer in the uploaded papers."

Write the answer in a clear, concise, and professional manner.

Context:
--------------------
{context}

Question:
{query}
"""

    answer = invoke_llm(prompt)

    return answer, docs