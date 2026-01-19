"""A simple script that demonstrates how to use the OpenAI API to generate chat completions.

This script shows the basic pattern for making a chat completion request:
1. Get an authenticated client
2. Define your messages (system + user)
3. Call the API
4. Print the response
"""

from src.openai_client import get_client


def main():
    """Send a simple chat message and print the response."""
    # Get authenticated client
    client = get_client()

    # Create a chat completion
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.7,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "What's the weather like in Bogota today?",
            },
        ],
    )

    # Print the response
    print("\n✅ Chat completion successful!\n")
    print("Assistant response:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
