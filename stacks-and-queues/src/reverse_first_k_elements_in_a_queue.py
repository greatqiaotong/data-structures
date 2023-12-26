"""
Implement the function reverseK(queue, k) which takes a queue and a number “k” as input and reverses the first “k” elements of the queue.
- Output: The queue with first “k” elements reversed. Remember to return the queue itself!

In case the value of “k” is larger than the size of the queue, is smaller than 0, or if the queue is empty, simply return None instead.
"""
from src.Queue import MyQueue
from src.Stack import MyStack


def reverseK(queue: MyQueue, k: int) -> MyQueue:
    if queue.is_empty():
        return None
    if k > queue.size() or k < 0:
        return None

    stack = MyStack()
    for i in range(k):
        stack.push(queue.dequeue())
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    for i in range(queue.size() - k):
        queue.enqueue(queue.dequeue())
    return queue
