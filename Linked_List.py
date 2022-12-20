class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        # Instantiate a new node
        new_node = self.__Node(val)
        # Appending the new node
        new_node.next = self.__trailer
        self.__trailer.prev.next = new_node
        new_node.prev = self.__trailer.prev
        self.__trailer.prev = new_node
        # Increment list size value
        self.__size = self.__size+1

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        # Check if index zis too large (or at the tail) or negative
        if index > self.__size-1 or index < 0:
            raise IndexError
        # Instantiate a new node
        new_node = Linked_List.__Node(val)
        # Reach to the node before the one at the specified index
        if index < self.__size/2: # Index behind or in front of middle of the list?
            # Start at the header
            cur = self.__header
            for i in range(index):
                cur = cur.next
        else:
            # Start at the trailer
            cur = self.__trailer.prev
            for i in range(self.__size-index):
                cur = cur.prev
        # Insert the new node
        cur.next.prev = new_node
        new_node.prev = cur
        new_node.next = cur.next
        cur.next = new_node
        # Increment list size value
        self.__size = self.__size+1

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        # Check if index is too large or negative
        if index >= self.__size or index < 0:
            raise IndexError
        # Reach to the node at the specified index
        if index < self.__size/2:
            # Start at the header
            cur = self.__header.next
            for i in range(index):
                cur = cur.next
        else:
            #Start at the trailer
            cur = self.__trailer
            for i in range(self.__size-index):
                cur = cur.prev
        # Remove the node
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        cur.next = None
        cur.prev = None
        # Decrement list size value
        self.__size = self.__size-1
        return cur.val

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        # Check if index is too large or negative
        if index >= self.__size or index < 0:
            raise IndexError
        if index < self.__size/2:
            # Start at the header
            cur = self.__header.next
            for i in range(index):
                cur = cur.next
        else:
            #Start at the trailer
            cur = self.__trailer
            for i in range(self.__size-index):
                cur = cur.prev
        return cur.val

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        # Check if the list is empty
        if self.__size == 0:
            return
        # Get the original head
        node = self.__header.next
        # Link the header with the new head
        self.__header.next = node.next
        node.next.prev = self.__header
        # Append the original head as the new tail
        node.next = self.__trailer
        self.__trailer.prev.next = node
        node.prev = self.__trailer.prev
        self.__trailer.prev = node
        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        # Create a new list with the same size as the linked list
        # Check if the list is empty
        if self.__size == 0:
            return '[ ]'
        # Create a list to store strings to be joined into a returning string
        items = [None] * (self.__size*2+1)
        # The first two characters of the returning string
        items[0] = '[ '
        # To get the values from each node one at a time starting from the head
        cur = self.__header.next
        # Run through the list
        for i in range(1,self.__size*2,2):
            items[i]=str(cur.val) # The value of the current node
            items[i+1]=', ' # The seperator of each value in the returning string
            cur = cur.next # Next node
        # The last two characters of the returning string that replace a seperator ', '
        items[len(items)-1] = ' ]'
        return ''.join(items)

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.__iter_cur = self.__header
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.__iter_cur.next is self.__trailer:
            raise StopIteration
        else:
            self.__iter_cur = self.__iter_cur.next
        return self.__iter_cur.val

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        new_list = Linked_List()
        cur_original = self.__trailer.prev # To take values from the original list starting from the tail
        cur_new = new_list.__header # To add new nodes starting from the header
        for i in range(self.__size):
            cur_new.next = new_list.__Node(cur_original.val) # Append the value to the new list
            cur_original = cur_original.prev # Move backwards through the original list
            cur_new = cur_new.next # Move forwards through the new list
        # Link the of the new list trailer with the tail 
        cur_new.next = new_list.__trailer
        new_list.__trailer.prev = cur_new
        # Define the size the new list
        new_list.__size = self.__size
        return new_list

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests
    
    # Linked lists
    ll_5 = Linked_List() # 5 elements
    ll_5.append_element(0)
    ll_5.append_element(1)
    ll_5.append_element(2)
    ll_5.append_element(3)
    ll_5.append_element(4)
    ll_0 = Linked_List() # Empty
    ll_1 = Linked_List() # 1 element
    ll_1.append_element(0)

    # Test methods
    # ll_5.append_element('a')
    # ll_0.append_element('a')
    # ll_1.append_element('a')
    # ll_5.insert_element_at('b',0)
    # ll_1.insert_element_at('b',0)
    # ll_5.insert_element_at('c',3)
    # ll_0.insert_element_at('b',0) # Should raise error
    # ll_5.remove_element_at(0)
    # ll_1.remove_element_at(0)
    # ll_5.remove_element_at(3)
    # ll_0.remove_element_at(0) # Should raise error
    # print(ll_5.get_element_at(3))
    # print(ll_1.get_element_at(0))
    # ll_0.get_element_at(0) # Should raise error
    # for i in range(8):
    #     ll_5.rotate_left()
    # ll_1.rotate_left()
    # ll_0.rotate_left()
    # print(reversed(ll_5))
    # print(reversed(ll_1))
    # print(reversed(ll_0))
    # for i in range(8):
    #     print(i, reversed(ll_5))
    # for val in ll_5:
    #     print(val)
    # for val in ll_0:
    #     print(val)
    # for val in reversed(ll_5):
    #     print(val)
    
    # Show contents and size
    print(str(ll_5))
    print('size:', len(ll_5))
    print(str(ll_0))
    print('size:', len(ll_0))
    print(str(ll_1))
    print('size:', len(ll_1))
