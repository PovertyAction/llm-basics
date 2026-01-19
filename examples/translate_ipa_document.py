"""Translate the IPA Best Bets document from English to Spanish.

This script:
- Reads the IPA Best Bets document in English
- Translates it to Spanish using OpenAI
- Saves the Spanish version to the data folder
"""

from pathlib import Path

from src.openai_client import get_client


def translate_to_spanish(text: str) -> str:
    """Translate English text to Spanish using OpenAI.

    Args:
        text: The English text to translate

    Returns:
        The translated Spanish text

    """
    client = get_client()

    response = client.chat.completions.create(
        model="gpt-4o",  # Using gpt-4o for better quality on long documents
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional translator specializing in academic and policy documents. "
                    "Translate the following document from English to Spanish. "
                    "Maintain the markdown formatting exactly as it appears. "
                    "Use formal, professional Spanish appropriate for policy and research documents. "
                    "Preserve all technical terms and proper nouns appropriately."
                ),
            },
            {
                "role": "user",
                "content": f"Translate this document to Spanish:\n\n{text}",
            },
        ],
        temperature=0.3,  # Lower temperature for more consistent translation
    )

    return response.choices[0].message.content


def main():
    """Translate the IPA Best Bets document and save to data folder."""
    # Define file paths
    input_file = Path("data/ipa-best-bets-2025.md")
    output_file = Path("data/ipa-best-bets-2025-es.md")

    print(f"\n📖 Reading {input_file}...")

    # Read the English document
    with open(input_file, encoding="utf-8") as f:
        english_text = f.read()

    print(f"✅ Document loaded ({len(english_text)} characters)")
    print("\n🔄 Translating to Spanish (this may take a moment)...")

    # Translate to Spanish
    spanish_text = translate_to_spanish(english_text)

    print(f"✅ Translation complete ({len(spanish_text)} characters)")

    # Create data directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Save the Spanish translation
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(spanish_text)

    print(f"\n💾 Spanish version saved to: {output_file}")
    print("\n✨ Translation complete!\n")


if __name__ == "__main__":
    main()
