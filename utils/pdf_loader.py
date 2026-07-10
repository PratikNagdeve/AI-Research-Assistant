import fitz  # PyMuPDF


def extract_text_from_pdf(uploaded_file):
    """
    Extract text page by page from a PDF.

    Returns:
        List of dictionaries:
        [
            {
                "page": 1,
                "text": "...",
                "source": "paper.pdf"
            },
            ...
        ]
    """

    pages = []

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)

        text = page.get_text()

        pages.append(
            {
                "page": page_num + 1,
                "text": text,
                "source": uploaded_file.name,
            }
        )

    pdf.close()

    return pages