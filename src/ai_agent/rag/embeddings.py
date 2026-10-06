from openai import OpenAI

from ..config import settings


def create_embedding(content: str) -> list[float]:
    """Create an embedding through an OpenAI-compatible endpoint."""
    client = OpenAI(base_url=settings.base_url, api_key=settings.api_key)
    response = client.embeddings.create(model=settings.embedding_model, input=content)
    return response.data[0].embedding
