from src.openai_client import get_client

def translate_to_english(text):
    client = get_client()
    response = client.responses.create(
        model="gpt-5-mini",
        input=[
            {"role": "developer", "content": "You are a professional translator."},
            {"role": "user", "content": f"Translate the following text to English:\n{text}"}
        ]
    )
    return response.output_text