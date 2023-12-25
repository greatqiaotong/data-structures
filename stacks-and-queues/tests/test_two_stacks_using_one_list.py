from src.two_stacks_using_one_list import TwoStacks


def test_two_stacks():
    stacks = TwoStacks(5)
    assert stacks.size == 5
    assert stacks.arr == [0, 0, 0, 0, 0]
    assert stacks.top1 == -1
    assert stacks.top2 == 5

    stacks.push1(6)
    stacks.push1(3)
    stacks.push1(2)
    stacks.push2(4)
    stacks.push2(5)
    assert stacks.size == 5
    assert stacks.arr == [6, 3, 2, 5, 4]
    assert stacks.top1 == 2
    assert stacks.top2 == 3

    x = stacks.pop1()
    assert x == 2
    assert stacks.size == 5
    assert stacks.arr == [6, 3, 2, 5, 4]
    assert stacks.top1 == 1
    assert stacks.top2 == 3

    x = stacks.pop2()
    assert x == 5
    assert stacks.size == 5
    assert stacks.arr == [6, 3, 2, 5, 4]
    assert stacks.top1 == 1
    assert stacks.top2 == 4
