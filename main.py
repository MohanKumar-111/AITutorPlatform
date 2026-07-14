import json
from openai import OpenAI

# Replace with your API key
client = OpenAI(api_key="YOUR_API_KEY")

# Get user input
question = input("Ask your question: ")

# Error handling for empty input
if not question.strip():
    print("Error: Question cannot be empty.")
    exit()

try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "You are a helpful teacher who explains concepts step-by-step. Always give an Explanation and an Example."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    answer = response.output_text

    print("\n===== AI Response =====")
    print(answer)

    # Save conversation to JSON
    conversation = {
        "question": question,
        "answer": answer
    }

    try:
        with open("history.json", "r") as file:
            history = json.load(file)
    except:
        history = []

    history.append(conversation)

    with open("history.json", "w") as file:
        json.dump(history, file, indent=4)

    print("\nConversation saved to history.json")

except Exception as e:
    print("API Error:", e)
