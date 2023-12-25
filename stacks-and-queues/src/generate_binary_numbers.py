from src.Queue import MyQueue


# number is a positive integer
def find_bin(number):
    result = []
    queue = MyQueue()
    queue.enqueue("1")

    for i in range(number):
        result.append(str(queue.dequeue()))
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        queue.enqueue(s1)
        queue.enqueue(s2)

    return result
