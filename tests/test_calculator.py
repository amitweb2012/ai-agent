from ai_agent.tools.calculator import CalculatorTool

def test_calculator():
    assert CalculatorTool().execute(expression="2 + 3 * 4").output == 14
