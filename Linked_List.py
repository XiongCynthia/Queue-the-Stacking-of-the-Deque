class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0

    def __len__(self):
        return self.__size

    def append_element(self, val):
        # This is the only way to add items at the tail position.
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
        # Check if index is too large (or at the tail) or negative
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
        # Rotate the list left one position (e.g., [ 5, 7, 9, -4 ] to [ 7, 9, -4, 5 ]).
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
        self.__iter_cur = self.__header
        return self

    def __next__(self):
        if self.__iter_cur.next is self.__trailer:
            raise StopIteration
        else:
            self.__iter_cur = self.__iter_cur.next
        return self.__iter_cur.val

    def __reversed__(self):
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
    pass
