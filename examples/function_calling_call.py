"""Demonstrates function calling with actual execution.

This script shows how to:
- Declare a function schema (lookup_weather)
- Have the model decide when to call the function
- Parse tool call responses
- Actually execute the function that the model requested

This extends the basic example by executing the function call.
"""

import json

from src.openai_client import get_client


def lookup_weather(city_name=None, zip_code=None):
    """Lookup the weather for a given city name or zip code.

    Args:
        city_name: The city name (optional)
        zip_code: The zip code (optional)

    Returns:
        str: A weather description with temperature in Celsius (mock data)

    """
    location = city_name or zip_code
    print(f"🌤️  Looking up weather for {location}...")

    # Mock weather data - in a real app, you'd call a weather API here
    return "Currently 18°C and partly cloudy"


def main():
    """Demonstrate function calling with execution."""
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
            {"role": "user", "content": "What's the temperature in Celsius in Bogota?"},
        ],
        tools=tools,
        tool_choice="auto",
    )

    # Check if the model chose to call a function
    print("\n✅ Function calling with execution:\n")

    if response.choices[0].message.tool_calls:
        # Model decided to call a function
        tool_call = response.choices[0].message.tool_calls[0]
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print(f"Model chose to call: {function_name}")
        print(f"Arguments: {arguments}\n")

        # Execute the function
        if function_name == "lookup_weather":
            result = lookup_weather(**arguments)
            print(f"Function result: {result}")
    else:
        # Model responded with text instead
        print("Model responded with text instead of calling a function:")
        print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
