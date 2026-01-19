"""Demonstrates basic function calling with the OpenAI API.

This script shows how to:
- Declare a function schema (lookup_weather)
- Have the model decide when to call the function
- Parse tool call responses

Note: This example does NOT actually execute the function—it just shows
how the model identifies when and how to call it.
"""

from src.openai_client import get_client


def main():
    """Demonstrate basic function calling without execution."""
    # Get authenticated client
    client = get_client()

    # Define the function schema (tools)
    tools = [
        {
            "type": "function",
            "function": {
                "name": "lookup_weather",
                "description": "Lookup the weather for a given city name or zip code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_name": {
                            "type": "string",
                            "description": "The city name",
                        },
                        "zip_code": {
                            "type": "string",
                            "description": "The zip code",
                        },
                    },
                    "additionalProperties": False,
                },
            },
        }
    ]

    # Make API call with tools parameter
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful weather assistant."},
            {"role": "user", "content": "What's the weather like in Berkeley?"},
        ],
        tools=tools,
    )

    # Check if the model chose to call a function
    print("\n✅ Function calling example:\n")

    if response.choices[0].message.tool_calls:
        # Model decided to call a function
        tool_call = response.choices[0].message.tool_calls[0]
        print(f"Model chose to call: {tool_call.function.name}")
        print(f"Arguments: {tool_call.function.arguments}")
        print("\nNote: In a real application, you would now execute this function")
        print("and send the results back to the model.")
    else:
        # Model responded with text instead
        print("Model responded with text instead of calling a function:")
        print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
