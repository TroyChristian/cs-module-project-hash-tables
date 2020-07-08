class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    
    def remove_node(self, value):
        current_node = self.head

        previous_node = current_node
        current_node = current_node.next

        if current_node.value == value:
            self.head = self.head.next 
            return current_node

        while current_node is not None:
            if current_node.value == value:
                previous_node = current_node.next 
                return current_node
            
            else:
                previous_node = previous_node.next
                current_node = current_node.next
        return None 

    
    def seek(self, value):
        current_node = self.head

        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next 


        