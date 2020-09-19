"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete():
        # point neighbor nodes to each other
        if self.prev:
            self.next.prev = self.prev
        if self.next:
            self.prev.next = self.next
            
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
        new_node = ListNode(value)
        #If DLL is empty, the new node is the head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #If DLL has at least one node
        else:
            self.head.prev = node
            self.head = self.head.prev
        #Update length
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #If the DLL is empty, return nothing
        if self.head is None:
            return
        #If DLL is not empty:
        else:
            #set head to the 2nd item
            self.head = self.head.next
            #save a copy of the original head (for return)
            original_head = self.head.prev
            #delete pointers to the previous head
            self.head.prev.delete()
        #return the original head's value
        return original_head.value
            
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
        #if the node is alrady the head, do nothing
        if self.head is node:
            return
        #set a location for iterating through the nodes of the list
        loc = self.head
        #move right through nodes until input node is found in list
        #or until we reach the end of the list
        while loc.right is not None:
            #if we've found the input node in the list
            if loc == node:
                #connect neighbors of input node to each other (left/right pointers should connect)
                node.delete()
                #set input node as left of head and set old head as right of input node
                self.add_to_head(node.value)
                #return True because node was found in list
            #if we haven't found the node yet, we move right
            else:
                #move right
                loc = loc.right
        #Return false because input node was not found in list
        return False
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        #set a location for iterating through the nodes from the far left

        #move right until the input node is found in the list 
        #or until we reach the end of the list

        #if we've found the input node in the list

            #break left/right bonds between input node and its neighbors

            #connect input node's neighbors
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #don't need to return value

        #do need to update head, tail
        if self.head is None:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head: #to get to this if/else statement, the list has to be at least 2 nodes
            self.head = self.head.next
            node.next.prev = None
            node.next = None
        
        self.length -= 1
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
                
                