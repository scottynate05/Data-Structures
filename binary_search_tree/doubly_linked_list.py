"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def set_next(self, value):
        self.next = value
            
    def get_next(self):
        return self.next
    
    def get_value(self):
        return self.value
    
    def set_prev(self, value):
        self.prev = value
    
    def get_prev(self):
        return self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
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
        self.length += 1

        # check if empty
        if self.head is None and self.tail is None:
           self.head = new_node
           self.tail = new_node
           print('node inserted')
        # current head pointed to by new node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        head = self.head.get_value()
        self.delete(self.head)
        return head
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        # check if empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # current tail pointed to by new node
        else:
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        tail = self.tail.get_value()
        self.delete(self.tail)
        return tail
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is None or self.head is None or self.head is node:
            pass
        else:
            node.next = self.head
            self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is None or self.head is None or self.tail is node:
            pass
        else:
            value = node.value
            self.delete(node)
            self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is None or self.head is None:
            return
        self.length -= 1
        if self.head is self.tail and node is self.head:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.get_next()
            self.head.set_prev(None) 
        elif node == self.tail:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

        else:
            node.delete()
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head and self.tail is None:
            return None
        
        maxVal = self.head.get_value()
        curNode = self.head
        for i in range(self.length):
            if curNode.get_value() > maxVal:
                maxVal = curNode.get_value()
            curNode = curNode.get_next()
            print(maxVal)
        return maxVal

dub_lin_list = DoublyLinkedList()
dub_lin_list.add_to_head(10)
dub_lin_list.add_to_head(104)
dub_lin_list.get_max()