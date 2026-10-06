from ai_agent.rag.cosine_similarity import cosine_similarity
from ai_agent.rag.retriever import load_documents


def test_cosine_similarity():
    assert cosine_similarity([1, 0], [1, 0]) == 1.0


def test_knowledge_documents_loaded():
    documents = load_documents()
    assert "python.txt" in documents
