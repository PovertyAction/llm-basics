"""Adds a back-and-forth chat interface using input() which keeps track of past messages and sends them with each chat completion call.

This script demonstrates:
- Maintaining conversation history across multiple turns
- How LLMs are stateless (you must send full history each time)
- Interactive chat loop with user input
- Building context over multiple exchanges

Type 'quit' or 'exit' to end the conversation.
"""

from src.openai_client import get_client


def main():
    """Run an interactive chat session with conversation history."""
    # Get authenticated client
    client = get_client()

    # Initialize conversation with system message
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Be concise and friendly.",
        },
    ]

    print("\n✅ Chat session started!")
    print("Type 'quit' or 'exit' to end the conversation.\n")

    # Chat loop
    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Check for exit commands
        if user_input.lower() in ["quit", "exit"]:
            print("\nGoodbye! 👋\n")
            break

        if not user_input:
            continue

        # Add user message to history
        messages.append({"role": "user", "content": user_input})

        # Get response from API (sending full conversation history)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
        )

        # Extract assistant's reply
        bot_response = response.choices[0].message.content

        # Add assistant message to history
        messages.append({"role": "assistant", "content": bot_response})

        # Print response
        print(f"\nAssistant: {bot_response}\n")


if __name__ == "__main__":
    main()
