

""" 
    Information regarding dequeue subclass of collections class
        1. Dequeue is used as a collection where we can enter from both sides of the array
        2. There are a lot of fuctions/methods defined for the class to perform as both stack data structure 
            and as queue data structure.
    Notable functions:
        1. append() method
            : append to the last of the deque
        2. appendleft() method
            : append to the start of the deque
        3. clear() method
            : remove all the elements from the deque leaving length to be zero
        4. count(x) method
            : return the number of elements in deque x
        5. extend(iterable) method
            : append to the end of the deque the elements present in iterable
                iterable : an array or some data type on which iteration/ looping can happen
        6. extendleft(iterable) method
            : append to the start of the deque the elements present in iterable
        7. index(x, [start,stop]) method
            : returns the position of x in start <-> stop (start inclusive)
        8. insert(i,x) method
            : insert i at position x
        9. pop() method
            : returns last value in deque
        10. popleft() method
            : return first value in deque
        11. remove(x) method
            : remove first occurrence of x from deque , returns None
        12. reverse() method
            : reverses deque
        13. rotate(n = 1) method
            : rotates the deque n steps to the right
                if n is negative: 
                    rotates n steps to the left
        14. maxlen() method
            : returns maxlen of deque
        

"""


"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""


class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        pass

    def peek(self):
        pass

    def dequeue(self):
        pass


def dequeue_test():
    # Setup
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test peek
    # Should be 1
    print(q.peek())

    # Test dequeue
    # Should be 1
    print((q.dequeue()))

    # Test enqueue
    q.enqueue(4)
    # Should be 2
    print(q.dequeue())
    # Should be 3
    print(q.dequeue())
    # Should be 4
    print(q.dequeue())
    q.enqueue(5)
    # Should be 5
    print(q.peek())
