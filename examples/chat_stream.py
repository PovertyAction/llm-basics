"""Adds stream=True to the API call to return a generator that streams the completion as it is being generated.

This script demonstrates streaming responses, which:
- Show tokens appearing progressively (like ChatGPT interface)
- Provide better user experience for long responses
- Use the same API call with stream=True parameter
"""

from src.openai_client import get_client


def main():
    """Send a chat message and stream the response as it's generated."""
    # Get authenticated client
    client = get_client()

    # Create a streaming chat completion
    completion_stream = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.7,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "Write a short description of the poverty probability index.",
            },
        ],
        stream=True,
    )

    # Stream and print the response as it arrives
    print("\n✅ Streaming response:\n")
    for event in completion_stream:
        if event.choices:
            content = event.choices[0].delta.content
            if content:
                print(content, end="", flush=True)

    print("\n")  # Add newline at the end


if __name__ == "__main__":
    main()
