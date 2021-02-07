
"""
    A stack is a data structure which follows the principle of Last In First Out, 
    i.e if you can push at top and pop from top.
    They both get completed in O(1) time.
"""

# Implementation of stack with array due to inbuilt
# functionality of python
# Append function will work as push as it appends to last
# pop function will work to get last elemnt


from linkedList import *
stack = [1, 2, 3]
stack.append(4)

print(stack)  # results [1, 2, 3, 4]

stack.pop()
print(stack)  # results [1, 2, 3]


# A stack can also be implemnted using a linked list
# time complexity still remains same


class Stack(object):
    def __init__(self, top=None):
        self.ll = Linked_list(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()


def stack_test():

    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a Stack
    stack = Stack(e1)

    # Test stack functionality
    stack.push(e2)
    stack.push(e3)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop())
    stack.push(e4)
    print(stack.pop().value)


stack_test()
