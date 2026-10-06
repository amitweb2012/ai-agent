from openai import OpenAI

from ..config import settings
from .tool_manager import execute_tool

ROLES = {
    "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",
    "2": "You are a senior Python developer. Explain programming concepts clearly and include Python examples.",
    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",
    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",
    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer.",
}


def main() -> None:
    client = OpenAI(base_url=settings.base_url, api_key=settings.api_key)
    print("Welcome to the AI Assistant! Type 'exit' to quit.")
    print("1. Teacher\n2. Python Expert\n3. Travel Guide\n4. Motivational Coach\n5. Interviewer")
    choice = input("\nEnter your choice: ").strip()
    messages = [{"role": "system", "content": ROLES.get(choice, "You are a helpful AI assistant.")}]

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        tool_result = execute_tool(user_input)
        if tool_result:
            print(f"AI: {tool_result}")
            continue
        messages.append({"role": "user", "content": user_input})
        response = client.chat.completions.create(model=settings.model, messages=messages)
        answer = response.choices[0].message.content or "The model returned an empty answer."
        print(f"AI: {answer}")
        messages.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    main()
