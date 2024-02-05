import json
import random


# Get recent messages
def get_recent_messages():
    # Define the file name and learn instructions
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": """
        You are guiding the user on a journey to discover their dream career. Start by asking the user's name.
        Keep the language simple, use easy-to-understand grammar, and maintain a friendly tone. Your name is Caleb,
        the career sunshine. Make the conversation interactive and add a random element to keep it fun. Encourage
        the user to share their interests. Responses should be concise, under 30 words.
        """
    }

    # Initialize messages
    messages = []

    # Add a random element
    x = random.uniform(0, 1)
    if x < 0.25:
        learn_instruction["content"] += " Inject a burst of positivity in your responses. Imagine a sunny day!"
    elif 0.25 <= x < 0.5:
        learn_instruction["content"] += " Let's add a sprinkle of curiosity. Ask about a surprising hobby!"
    elif 0.5 <= x < 0.75:
        learn_instruction["content"] += " Express excitement like discovering a treasure. Use exclamations!"
    else:
        learn_instruction["content"] += " Drop a hint of mystery. Pose a question with a touch of intrigue!"

    # Append instruction to message
    messages.append(learn_instruction)

    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append last 5 items of data
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)

                else:
                    for item in data[-5:]:
                        messages.append(item)

    except Exception as e:
        print(e)
        pass

    # Return
    return messages


# Store Messages
def store_messages(request_message, response_message):
    # Define file name
    file_name = "stored_data.json"

    # Get recent messages

    messages = get_recent_messages()[1:]

    # Add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant)

    # Save the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f)


def reset_messages():
    # Overwrite current file with nothing
    open("stored_data.json", "w")
