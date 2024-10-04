import os
import json
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # Use your OpenAI API key
)


# Define a function that returns flight information between two cities (mock implementation)
def get_flight_info(origin_city: str, destination_city: str):
    if origin_city == "Seattle" and destination_city == "Miami":
        return json.dumps(
            {
                "airline": "Delta",
                "flight_number": "DL123",
                "flight_date": "May 7th, 2024",
                "flight_time": "10:00AM",
            }
        )
    return json.dumps({"error": "No flights found between the cities"})


# Define the function tool with function calling support
tool = {
    "name": "get_flight_info",
    "description": """Returns information about the next flight between two cities.
                      This includes the name of the airline, flight number, and the date and time
                      of the next flight.""",
    "parameters": {
        "type": "object",
        "properties": {
            "origin_city": {
                "type": "string",
                "description": "The name of the city where the flight originates",
            },
            "destination_city": {
                "type": "string",
                "description": "The flight destination city",
            },
        },
        "required": ["origin_city", "destination_city"],
    },
}

# Prepare the messages for the chat completion
messages = [
    {
        "role": "system",
        "content": "You are an assistant that helps users find flight information.",
    },
    {
        "role": "user",
        "content": "I'm interested in going to Miami. What is the next flight there from Seattle?",
    },
]

# Create the initial chat completion using the gpt-4o model
response = client.chat.completions.create(
    model="gpt-4o", messages=messages, functions=[tool]
)

# Check if the response requires a function call
if response.choices[0].finish_reason == "function_call":
    # Parse the function call details
    function_call = response.choices[0].message.function_call
    function_name = function_call.name
    function_args = json.loads(function_call.arguments)

    # Call the function and get the result
    function_result = get_flight_info(**function_args)
    print(f"Function `{function_name}` returned: {function_result}")

    # Append the function result back to the chat history
    messages.append(
        {
            "role": "function",
            "name": function_name,
            "content": function_result,
        }
    )

    # Get a response from the model using the updated messages
    final_response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )

    # Print the final model response
    print(f"Model response: {final_response.choices[0].message.content}")
