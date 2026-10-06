from ai_agent.memory import InMemoryConversationStore

def test_memory_round_trip():
    memory = InMemoryConversationStore()
    memory.add("s1", "user", "hello")
    memory.add("s1", "assistant", "hi")
    assert len(memory.history("s1")) == 2
