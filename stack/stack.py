"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from singly_linked_list.singly_linked_list import LinkedList, Node
class Stack:
    def __init__(self, size=0, storage=[]):
        self.size = 0
        self.storage = storage

    def __len__(self):
        if self.storage == LinkedList():
            node = self.storage.head
            while node.get_next() is not None:
                node = node.get_next()
                self.size +=1
        else:
            self.size = len(self.storage)
        
        return self.size

    def push(self, value):
        if self.storage == LinkedList():
            self.storage.add_to_tail(value)
        else:
            self.storage.append(value)

    def pop(self):
        if len(self) == 0:
            return None
        elif len(self) == 1:
            if self.storage == LinkedList():
                return self.storage.remove_head()
            else:
                # self.storage.remove(self.storage[0])
                return self.storage.pop()
        else:
            if self.storage == LinkedList():
                return self.storage.remove_tail()
            else:
                # self.storage.remove(self.storage[-1])
                return self.storage.pop()
