# Queue-the-Stacking-of-the-Deque

Array_Deque.py and Linked_List_Deque.py are two different deque implementations with identical functionalities. Stack.py and Queue.py are a stack and queue implementations, respectively, that can use a deque implementation from Array_Deque.py or Linked_List_Deque.py as the storage medium.

---

## Deque Performances

In the Array_Deque implementation, **\_\_init\_\_**, **\_\_len\_\_**, **pop_front**, **peek_front**, **pop_back**, and **peek_back** all operate in constant time since they only have operations involving getting values, assignment, instantiation, comparison, arithmetic, if-else statements, and raising errors. No particular case can affect the methods’ runtimes in some significant way.

Except for \_\_str\_\_, all of the methods of the Linked_List_Deque implementation all operate in constant time. Although insert_element_at, remove_element_at, and get_element_at operate in linear time by going through the list to reach the specified index, in Linked_List_Deque, the index is always the same, and the runtime to reach it is never affected by array size or some other factor. All other operations in all methods are also constant time.

The methods **\_\_str\_\_** from both implementations and **\_\_grow** from Array_Deque operate in linear time. So does the **push_front** and **push_back** methods from Array_Deque, but only when the specified array is full since that condition invokes __grow. They involve going through the entire array each element at a time, so a longer array would mean more elements to go through, and thus increasing the runtime. Additionally, all other operations are constant time, so the methods cannot be in quadratic time.

The __grow method doubles the array capacity instead of simply increasing it by one cell. If this latter strategy were used, when adding multiple elements, it would require moving every element into a larger array one by one as many times as there are new elements to add, meaning any case where multiple elements are to be added would lead to quadratic time instead of linear time. Doubling array capacity would provide pre-allocated spaces to add new elements, significantly diminishing how often elements are relocated when adding a large quantity of new ones.


## Stack and Queue Performances

The runtime of certain methods may depend on whether the Array_Deque or Linked_List_Deque is used. The **\_\_str\_\_** method always operates on linear time, and the **\_\_len\_\_**, **pop**, **dequeue**, and **peek** methods always operate in constant time. The **push** and **enqueue** methods may operate in linear time in certain cases only when using the Array_Deque implementation, specifically when the capacity of the stack or queue object is full, which is when it invokes the __grow method that runs in linear time. They always operate in constant time otherwise and in the Linked_List_Deque implementation.

In my opinion, the design decision to not raise exceptions in any of the methods in the Stack and Queue implementations is worse than not having it in Array_Deque or Linked_List_Deque. It does make more sense to notify the problem that is closer to the “core,” but it also makes the problem more vague to the user. For example, when attempting to remove an element from an empty stack or queue, an IndexError does little to tell the user what it means in the context of an object that does not take indices to get elements.

