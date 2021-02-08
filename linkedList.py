

# TODO: create a linked list :
# * A linked list is a data structure containing a value and a pointer to next element

# element of a linked list
class Element(object):

    def __init__(self, value):
        super().__init__()
        self.value = value
        self._next = None

    def get_Value(self):
        return self.value

    def get_Next(self):
        return self._next

# class of linked list


class Linked_list(object):

    def __init__(self, head=None):
        super().__init__()
        self.head = head

    def get_Head(self):
        return self.head

    # adding a new element to linked list in last
    def append(self, new_element):
        """ @input: a new element having a value and next
            Add the element to the last of the linked list
            @retrun None
        """
        current = self.head
        if current:
            # traverse till the last element
            while current._next:
                current = current._next

            # add the element at last
            current._next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

        # points to the start of the list
        current = self.head
        # value to be returned
        return_value = None
        if current:
            # to maintain number of elements traversed in the list
            count = 1
            found = False
            while current:  # idea is to traverse as long as there are elements in the list
                if(position == count):
                    found = True
                    return_value = current
                    break
                else:
                    current = current._next
                    count += 1
            # if element is not even after traversing whole list
            if(found == False):
                return_value = None

        else:
            return_value = None

        return return_value

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        # check whether list is empty or not
        if current:
            count = 1
            prev = current
            found = False
            # Traverse throgh list to find the position of insertion
            while current:
                if (position == count):
                    found = True
                    new_element._next = current
                    prev._next = new_element
                    break

                else:
                    prev = current
                    current = current._next
                    count += 1

            # inserting the element at last
            if(found == False and position == count+1):
                current._next = new_element
            else:
                return "Postion not available."

        else:
            if(position == 1):
                new_element.next = self.head
                self.head = new_element

            else:
                return "List Empty !!! Position not available"

    def delete(self, value):
        """Delete the first node with a given value."""

        current = self.head

        # check whether list is empty or not
        if current:

            count = 1
            found = False
            prev = current
            # Traverse through the list to find the first particular element with value
            while current:
                if(current.value == value):
                    if current._next:
                        if(count == 1):
                            self.head = current._next
                            current._next = None
                            break
                        else:
                            prev.next = current._next
                            current._next = None
                            break
                    else:
                        prev._next = None
                else:
                    prev = current
                    current = current._next
                    count += 1
            if (found == False):
                return "Value not present in the list"

        else:
            return "List is Empty!!! No values to delete"

    def print_list(self):
        """summary: prints a given list 

            Return: a string based representation of list
        """
        linked_list = ""
        # get a pointer to head
        current = self.head
        if current:
            # traverse the list and concatenate to string
            while current._next:
                linked_list += str(current.value)
                linked_list += "->"
                current = current._next
            linked_list += str(current.value)

        else:
            return "List is Empty"

        return linked_list

    def insert_first(self, new_element):
        """inserts a element to start to the list

        Args:
            new_element ([element]): [A new element with value and next as none to be added in list ])

        Return: return None 
        """
        new_element._next = self.head
        self.head = new_element

    def delete_first(self):
        """deletes the first element in the linked list and return it

        Return : returns the first element 
        """
        current = self.head
        if current:
            self.head = current._next
            current._next = None
            return current
        else:
            return "Nothing to delete"

    def delete(self, position):
        """deletes the element at given position if exists.
            ***position is 1 based***

        Args:
            position (int): position to be deleted
        """
        current = self.head
        if current:
            prev = current
            count = 1
            found = False
            while current:
                if(position == count):
                    found = True
                    if(count == 1):
                        self.head = current._next
                        current._next = None
                        return current
                    else:
                        if current._next:
                            prev.next = current._next
                        else:
                            prev._next = None
                else:
                    prev = current
                    current = current._next
                    count += 1

        else:
            return "Nothing to delete"

    def reverse(self):
        """ Reverses the linked list 
        """
        current = self.head
        reverse_head = self.head

        rest_of_list = current._next

        # check whether list is empty
        if current:
            # check whether list has only one element
            if current._next:
                reverse_head._next = None
                # traverse through rest of list and add it reverse head one by one
                while rest_of_list:
                    # node to be added in reversed list
                    to_be_reversed = rest_of_list
                    # rest of list remaining to be reversed
                    rest_of_list = rest_of_list._next

                    # add the node to head of reversed list
                    to_be_reversed._next = reverse_head
                    reverse_head = to_be_reversed

            self.head = reverse_head
        else:
            return "List is empty ! Nothing to reverse."


def Linked_list_Test():
    # Test cases
    # Set up some Elements
    a = [3,
         5,
         16,
         12,
         4,
         2,
         5,
         3,
         7,
         3,
         9,
         5,
         5,
         1,
         18,
         3,
         13]
    ll = Linked_list()
    for element in a:
        e = Element(element)
        ll.append(e)

    # Start setting up a LinkedList

    # ll.append(e2)
    # ll.append(e3)

    # Test get_position
    # Should print 3
    # print(ll.head._next._next.value)
    # # Should also print 3
    # print(ll.get_position(3).value)

    # Test insert
    # ll.insert(e4, 3)
    # Should print 4 now
    # print(ll.get_position(3).value)

    # # Test delete
    # ll.delete(1)
    # # Should print 2 now
    # print(ll.get_position(1).value)
    # # Should print 4 now
    # print(ll.get_position(2).value)
    # # Should print 3 now
    # print(ll.get_position(3).value)
    # print(ll.get_position(3).value)
    print(ll.print_list())
    ll.reverse()
    print(ll.print_list())


Linked_list_Test()
