import unittest


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node = None


class Queue:
    def __init__(self) -> None:
        self.__head: Node = None
        self.__tail: Node = None
        self.__length: int = 0
    
    def get_length(self):
        return self.__length

    def get_head(self):
        return self.__head.data

    def get_tail(self):
        return self.__tail.data

    def is_empty(self):
        return self.__head == None

    def enqueue(self, data):
        new_node = Node(data)
        if(self.is_empty()):
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__length +=1
    
    def dequeue(self):
        if(self.is_empty()):
            raise ValueError("Queue is empty")
        
        data = self.__head.data
        current_node = self.__head.next
        self.__head.next = None
        self.__head = current_node
        self.__length -=1
        return data


# Testing
    

class QueueTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue()
    
    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
    
    def test_enqueue(self):
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.get_head(), 10)
    
    def test_remove(self):
        self.queue.enqueue(10)
        self.queue.enqueue(15)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.get_length(), 3)
        data = self.queue.dequeue()
        self.assertEqual(data, 10)
        self.assertEqual(self.queue.get_length(), 2)
        self.assertEqual(self.queue.dequeue(), 15)

if __name__ == '__main__':
    unittest.main(verbosity=2)
