from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = []

    for page in pages:

        split_text = splitter.split_text(page["text"])

        for text in split_text:

            chunks.append(
                {
                    "text": text,
                    "page": page["page"],
                    "source": page["source"]
                }
            )

    return chunks