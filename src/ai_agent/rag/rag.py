import textwrap

from openai import OpenAI

from ..config import settings
from .cosine_similarity import cosine_similarity
from .embeddings import create_embedding
from .retriever import load_documents

TERMINAL_WIDTH = 76


def print_section(title: str) -> None:
    border = "=" * TERMINAL_WIDTH
    print(f"\n{border}\n{title.upper()}\n{border}")


def print_wrapped(text: str, indent: str = "  ") -> None:
    for line in text.splitlines():
        print(
            textwrap.fill(
                line,
                width=TERMINAL_WIDTH,
                initial_indent=indent,
                subsequent_indent=indent,
            )
            if line.strip()
            else ""
        )


def find_best_document(question_embedding: list[float], document_embeddings: dict[str, list[float]]) -> tuple[str | None, float]:
    best_document, best_score = None, -1.0
    for filename, embedding in document_embeddings.items():
        score = cosine_similarity(question_embedding, embedding)
        if score > best_score:
            best_document, best_score = filename, score
    return best_document, best_score


def generate_answer(client: OpenAI, question: str, filename: str, content: str) -> str:
    response = client.chat.completions.create(
        model=settings.model,
        messages=[
            {
                "role": "system",
                "content": "Answer using only the provided document. Do not invent facts. If the document does not contain the answer, say so.",
            },
            {"role": "user", "content": f"Question: {question}\n\nRelevant document ({filename}):\n{content}"},
        ],
    )
    return response.choices[0].message.content or "The model returned an empty answer."


def main() -> None:
    documents = load_documents()
    if not documents:
        print("No documents found in the knowledge directory.")
        return

    print_section("Local RAG Assistant")
    print_wrapped(f"Loaded {len(documents)} document(s). Similarity threshold: {settings.rag_min_similarity:.0%}")

    document_embeddings = {filename: create_embedding(content) for filename, content in documents.items()}
    client = OpenAI(base_url=settings.base_url, api_key=settings.api_key)

    while True:
        question = input("\nYou: ").strip()
        if question.lower() == "exit":
            print("Goodbye!")
            return
        if not question:
            continue

        filename, score = find_best_document(create_embedding(question), document_embeddings)
        context = documents.get(filename) if filename else None
        print(f"Retrieved: {filename or 'none'} | similarity={score:.4f}")

        if not filename or not context or score < settings.rag_min_similarity:
            print("I couldn't find a sufficiently relevant document to answer that.")
            continue

        print(f"AI: {generate_answer(client, question, filename, context)}")


if __name__ == "__main__":
    main()
