from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__head = 0
    self.__tail = 0
    self.__size = 0
    
  def __str__(self):
    # Check if the list is empty
    if self.__size == 0:
      return '[ ]'
    # Create a list to store strings to be joined into a returning string
    items = [None] * (self.__size*2+1)
    # The first two characters of the returning string
    items[0] = '[ '
    # To get the values from each node one at a time starting from the head
    cur = self.__head
    # Run through the list
    for i in range(1,self.__size*2,2):
        items[i]=str(self.__contents[cur]) # The value of the current index
        items[i+1]=', ' # The seperator of each value in the returning string
        cur = (cur+1)%self.__capacity # Next index
    # The last two characters of the returning string that replace a seperator ', '
    items[len(items)-1] = ' ]'
    return ''.join(items)
    
  def __len__(self):
    return self.__size

  def __grow(self):
    # Create a new array double the current capacity
    new_arr = [None] * self.__capacity*2
    # To get values from the array starting from the head
    cur = self.__head
    # Transfer elements of the old array into the new array
    for i in range(self.__capacity):
      new_arr[i] = self.__contents[cur]
      cur = (cur+1)%self.__capacity
    # Replace the old array with the new array
    self.__contents = new_arr
    # Update the head and tail indices
    self.__head = 0
    self.__tail = self.__size-1
    # Update array capacity
    self.__capacity = self.__capacity*2
    return
    
  def push_front(self, val):
    # Resize array if capacity at limit
    if self.__size >= self.__capacity:
      self.__grow()
    # Move the head index left
    self.__head = (self.__head-1)%self.__capacity
    # Assign the specified value at the new head location
    self.__contents[self.__head] = val
    # Update array size
    self.__size = self.__size+1
    
  def pop_front(self):
    if self.__size == 0: # Check if array is empty
      raise IndexError
    val = self.__contents[self.__head]
    self.__head = (self.__head+1)%self.__capacity # Move head index right
    self.__size = self.__size-1
    return val
    
  def peek_front(self):
    if self.__size == 0: # Check if array is empty
      raise IndexError
    return self.__contents[self.__head]
    
  def push_back(self, val):
    # Resize array if capacity at limit
    if self.__size >= self.__capacity:
      self.__grow()
    # Move the tail index right
    self.__tail = (self.__tail+1)%self.__capacity
    # Assign the specified value at the new head location
    self.__contents[self.__tail] = val
    # Update array size
    self.__size = self.__size+1
    return
  
  def pop_back(self):
    if self.__size == 0: # Check if array is empty
      raise IndexError
    val = self.__contents[self.__tail]
    self.__tail = (self.__tail-1)%self.__capacity # Move tail index left
    self.__size = self.__size-1
    return val

  def peek_back(self):
    if self.__size == 0: # Check if array is empty
      raise IndexError
    return self.__contents[self.__tail]

# if __name__ == '__main__':
#   pass
