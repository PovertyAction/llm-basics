"""Translation utilities (legacy - uses old API)."""

from src.openai_client import get_client


def translate_to_english(text):
    """Translate text to English using OpenAI API.

    Note: This function uses an outdated API that no longer exists.
    Use the examples in examples/translate_ipa_document.py instead.

    Args:
        text: Text to translate

    Returns:
        Translated text

    """
    client = get_client()
    response = client.responses.create(
        model="gpt-5-mini",
        input=[
            {"role": "developer", "content": "You are a professional translator."},
            {
                "role": "user",
                "content": f"Translate the following text to English:\n{text}",
            },
        ],
    )
    return response.output_text
