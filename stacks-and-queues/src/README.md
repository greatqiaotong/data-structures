# Stack

Stacks follow the *Last in First Out (LIFO)* ordering. Many famous algorithms such as *Depth First Search* and the *Expression Evaluation Algorithm* harness the functionality of Stacks.

Stacks are used:
* To backtrack to the previous task/state, for example, in **recursive code**
* To store a partially completed task, for example, when you are exploring two different paths on a *Graph& from a point while figuring out the smallest path to the target.

A typical Stack must offer the following functionalities:

| Function | What does it do? | Complexity |
|:---:|:---:|:---:|
| push(element) | Inserts an element at the top | *O(1)* |
| pop() | Removes an element from the top and returns it | *O(1)* |
| peek() | Returns the top element of the stack | *O(1)* |
| is_empty() | Returns a boolean 1 if the stack is empty | *O(1)* |
| size() | Returns the size of the stack | *O(1)* |

Stacks can be implemented using lists, or linked lists.

# Queue

Queues implement the FIFO (*First in First Out*) method.

Queues are used when:
* We want to prioritise something over another
* A resource is shred between multiple devices

A typical Queue needs the following set of functions to work perfectly:

| Function | What does it do? | Complexity |
|:---:|:---:|:---:|
| enqueue(element) | Inserts an element at the end of the queue | *O(1)* |
| dequeue() | Removes an element from the start of the queue | *O(n)* using list, *O(1)* using double linked list |
| front() | Returns the first element of the queue | *O(1)* |
| rear() | Returns the last element inserted into the queue | *O(1)* |
| is_empty() | Returns a boolean 1 if the queue is empty | *O(1)* |
| size() | Returns the size of the queue | *O(1)* |

Four most common types of queues:
* *Linear Queue*
* *Circular Queue*
* *Priority Queue* 
* *Double-ended Queue* - acts as a queue from both ends (front and back). It is a flexible data structure that provides enqueue and dequeue functionality on both end in *O(1)*.

Queues can be implemented using lists, linked lists, or even stacks.