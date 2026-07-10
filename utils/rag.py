from utils.chatbot import get_llm


def answer_question(vectorstore, query):

    docs = vectorstore.similarity_search(query, k=3)

    context = ""

    for doc in docs:
        context += doc.page_content + "\n\n"

    prompt = f"""
You are an AI Research Assistant.

Answer ONLY using the context below.

If the answer is not present in the context, say:
"I could not find the answer in the uploaded papers."

Context:
---------
{context}

Question:
{query}

Provide a clear and concise answer.
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content, docs