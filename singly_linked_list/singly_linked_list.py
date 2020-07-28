class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        #Empty LL
        if self.head is None:
            return None
        # LL w/ only one element
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # LL w/ two or more elements
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return value
        
    def remove_tail(self):
        #Empty LL
        if self.tail is None:
            return None
        #LL w/ only one element
        elif self.head == self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # LL w/ two or more elements
        else:
            value = self.tail.get_value()
            node = self.head
            while node.get_next() is not None:
                if node.get_next().get_next() is None:
                    self.tail = node
                else:    
                    node = node.get_next()
            return value

    def contains(self, value):
        node = self.head
        while node is not None:
            if node.get_value() == value:
                return True
            node = node.get_next()
        #We've reached the end of the list, return False
        return False
            
    def get_max(self):
        #empty list
        if self.head is None:
            return None
        #non-empty list
        node = self.head
        curr_max = self.head.get_value()
        while node is not None:
            if node.get_value() > curr_max:
                curr_max = node.get_value()
            node = node.get_next()
        
        return curr_max