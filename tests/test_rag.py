from ai_agent.rag import Document, InMemoryRetriever

def test_retriever():
    retriever = InMemoryRetriever([Document("1", "Python AI agents", {"source": "docs"})])
    assert retriever.search("Python")[0].id == "1"
