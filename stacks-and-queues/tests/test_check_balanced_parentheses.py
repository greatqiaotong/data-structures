from src.check_balanced_parentheses import is_balanced


def test_is_balanced():
    exp = "{[()]}(){}[]"
    assert is_balanced(exp)


def test_is_not_balanced():
    exp = "{([)]}(){}[]"
    assert is_balanced(exp) == False
