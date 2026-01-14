"""
Test that your local environment can successfully connect to the OpenAI API.

If this script runs without errors and prints a short response,
your setup is correct.
"""

from openai import OpenAI
import os

def main():
    # Check that the API key is available
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY not found. "
            "Did you create a .env file and load it correctly?"
        )

    # Initialize client
    client = OpenAI()

    # Simple prompt
    response = client.responses.create(
        model="gpt-5-mini",
        input="Say hello in one short sentence."
    )

    print("\n✅ Connection successful!\n")
    print("Model response:")
    print(response.output_text)

if __name__ == "__main__":
    main()
