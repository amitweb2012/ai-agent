from ai_agent.basic.tool_manager import execute_tool


def test_time_tool():
    assert execute_tool("What time is it?")


def test_unknown_tool():
    assert execute_tool("tell me a joke") is None
