from openai import OpenAI

from ..config import settings


def main() -> None:
    client = OpenAI(base_url=settings.base_url, api_key=settings.api_key)
    response = client.chat.completions.create(
        model=settings.model,
        messages=[{"role": "user", "content": "Write a Python function that returns the sum of even numbers in a list."}],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
