import os
import time

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError

load_dotenv()


def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.2,
        max_retries=3,
        timeout=60,
    )


def invoke_llm(prompt: str):
    """
    Invoke Gemini and always return plain text.
    Automatically retries if a temporary rate limit (429) occurs.
    """

    llm = get_llm()

    for attempt in range(3):

        try:
            response = llm.invoke(prompt)

            # Gemini returns plain string
            if isinstance(response.content, str):
                return response.content

            # Gemini returns structured blocks
            if isinstance(response.content, list):

                text = ""

                for item in response.content:

                    if isinstance(item, dict):

                        if item.get("type") == "text":
                            text += item.get("text", "")

                    elif hasattr(item, "text"):
                        text += item.text

                return text

            return str(response.content)

        except ChatGoogleGenerativeAIError as e:

            error_message = str(e)

            if "RESOURCE_EXHAUSTED" in error_message or "429" in error_message:

                wait_time = 25

                print(
                    f"⚠️ Gemini quota/rate limit reached. "
                    f"Retrying in {wait_time} seconds "
                    f"({attempt + 1}/3)..."
                )

                time.sleep(wait_time)
                continue

            raise

    raise Exception(
        "Failed to invoke Gemini after multiple retry attempts."
    )