from ai_agent.basic.tools import generate_password, roll_dice


def test_roll_dice_range():
    assert 1 <= roll_dice() <= 6


def test_password_length():
    assert len(generate_password(16)) == 16
