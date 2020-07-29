"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        node = ListNode(value, prev=None, next=self.head)
        self.head.prev = node
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        node = ListNode(value, prev=self.tail, next=None)
        self.tail.next = node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.tail = self.tail.prev
        self.length -= 1
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        try:
            forward = self.head
            backward = self.tail
            while forward is not backward or forward.prev is not backward:
                if forward is not node or backward is not node:
                    forward = forward.next
                    backward = backward.prev
                elif forward is node:
                    forward.prev.next = forward.next
                    forward.next.prev = forward.prev
                else:
                    backward.prev.next = backward.next
                    backward.next.prev = backward.prev
            self.add_to_head(node)
        except:
            return 'Node not found'
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        try:
            forward = self.head
            backward = self.tail
            while forward is not backward or forward.prev is not backward:
                if forward is not node or backward is not node:
                    forward = forward.next
                    backward = backward.prev
                elif forward is node:
                    forward.prev.next = forward.next
                    forward.next.prev = forward.prev
                else:
                    backward.prev.next = backward.next
                    backward.next.prev = backward.prev
            self.add_to_tail(node)
        except:
            return 'Node not found'
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        try:
            forward = self.head
            backward = self.tail
            while forward is not backward or forward.prev is not backward:
                if forward is not node or backward is not node:
                    forward = forward.next
                    backward = backward.prev
                elif forward is node:
                    forward.prev.next = forward.next
                    forward.next.prev = forward.prev
                else:
                    backward.prev.next = backward.next
                    backward.next.prev = backward.prev
        except:
            return 'Node not found'

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        forward = self.head
        backward = self.tail
        curr_max = self.head if self.head >= self.tail else self.tail
        while forward is not backward or forward.prev is not backward:
            if forward >= curr_max:
                if backward >= curr_max:
                    curr_max = forward if forward >= backward else backward
                else:
                    curr_max = forward
            forward = forward.next
            backward = backward.prev
        
        return curr_max
                
                