from src.eval_postfix_expression import eval_post_fix
from src.Stack import MyStack


def test_eval_post_fix_empty_sequence():
    exp = ""
    result = eval_post_fix(exp)
    assert result == "Invalid sequence"


def test_eval_post_fix():
    exp = "921*-8-4+"
    result = eval_post_fix(exp)
    assert result == 3
