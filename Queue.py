from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    return str(self.__dq)

  def __len__(self):
    return len(self.__dq)

  def enqueue(self, val):
    self.__dq.push_back(val)

  def dequeue(self):
    if len(self.__dq) == 0:
      return None
    return self.__dq.pop_front()

  def peek(self):
    if len(self.__dq) == 0:
      return None
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
  
