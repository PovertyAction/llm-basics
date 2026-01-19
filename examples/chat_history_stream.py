"""The same idea as chat_history.py, but with stream=True enabled.

This script combines:
- Conversation history management (remembering past messages)
- Streaming responses (progressive token display)
- Interactive chat interface

This is the most production-like example, closest to how real chatbots work.

Type 'quit' or 'exit' to end the conversation.
"""

from src.openai_client import get_client


def main():
    """Run an interactive chat session with conversation history and streaming responses."""
    # Get authenticated client
    client = get_client()

    # Initialize conversation with system message
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Be concise and friendly.",
        },
    ]

    print("\n✅ Chat session started (streaming mode)!")
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

        # Get streaming response from API (sending full conversation history)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            stream=True,
        )

        # Stream and collect the response
        print("\nAssistant: ", end="", flush=True)
        bot_response = ""
        for event in response:
            if event.choices and event.choices[0].delta.content:
                content = event.choices[0].delta.content
                print(content, end="", flush=True)
                bot_response += content

        print("\n")  # Add newline after streaming completes

        # Add assistant message to history
        messages.append({"role": "assistant", "content": bot_response})


if __name__ == "__main__":
    main()
