import unittest


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__length: int = 0

    def get_length(self):
        return self.__length

    def is_empty(self):
        return self.__head == None

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.__head = self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node
        self.__length +=1

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.__head = self.__tail = new_node
        else:
            current_node = self.__head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
            new_node = None
        self.__length +=1

    def remove_first(self):
        if self.is_empty():
            raise ValueError("Linked is Empty")
        if self.__head==self.__tail:
            data = self.__head.data
            self.__head=self.__tail=None
            return data
        data = self.__head.data
        current_node = self.__head.next
        self.__head.next = None
        self.__head = current_node
        return data
        
    def remove_last(self):
        if self.__head == None:
            raise ValueError("linked list is empty")
        if self.__head==self.__tail:
            data = self.__head.data
            self.__head=self.__tail=None
            return data

        previous_node = self.__head
        current_node = self.__head.next

        while current_node != None:
            previous_node = current_node
            current_node = current_node.next

        data = current_node.data
        previous_node.next = None
        return data

    def add_at(self, index, data):
        if index > self.__length or index < 0:
            raise IndexError("Index is invalid")
        if index == 0:
            self.add_first(data)
        else:
            new_node = Node(data)
            current_node  = self.__head
            current_index = 1
            while(current_node != None):
                if current_index == index:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return
                current_index +=1
                current_node = current_node.next
        self.__length +=1

    def remove_at(self, index):
        if index > self.__length or index < 0:
            raise IndexError("Index is invalid")
        
        if index == 0:
            return self.remove_first()

        previous_node = self.__head
        current_node = previous_node.next
        current_index = 1
        while(current_node != None):
            if current_index == index:
                previous_node.next = current_node.next
                current_node.next = None
                return current_node.data
            previous_node = current_node
            current_node = current_node.next
            current_index +=1


    def get(self, index):
        if index > self.__length or index < 0:
            raise IndexError("Index is invalid")

        current_node = self.__head
        current_index = 0
        while current_node != None:
            if current_index == index:
                return current_node.data
            current_node = current_node.next
            current_index +=1

    def to_simple_list(self):
        if self.__head == None:
            return None
        else:
            data = []
            current_node = self.__head
            while current_node.next !=None:
                data.append(current_node.data)
                current_node = current_node.next
            data.append(current_node.data)

        return data


# Unit Testing


class LinkedLiestTestCase(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.linked_list.add_last(10)
        self.linked_list.add_last(20)
        self.linked_list.add_last(30)
        self.linked_list.add_last(40)

    def test_add_last(self):
        self.assertTrue(callable(self.linked_list.add_last))
        self.linked_list.add_last(50)
        self.assertEqual(self.linked_list.get_length(), 5)

    def test_to_simple_list(self):
        self.assertEqual(self.linked_list.to_simple_list(), [10, 20, 30, 40])

    def test_add_at(self):
        self.linked_list.add_at(1, 15)
        self.assertEqual(self.linked_list.get(1), 15)
        self.assertEqual(self.linked_list.get(4), 40)
    
    def test_remove_at(self):
        data = self.linked_list.remove_at(1)
        self.assertEqual(data,20)
        self.assertEqual(self.linked_list.to_simple_list(), [10, 30, 40])

if __name__=="__main__":
    unittest.main(verbosity=2)