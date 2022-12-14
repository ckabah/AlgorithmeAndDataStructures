import unittest


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node = None


class Stack:
    def __init__(self) -> None:
        self.__top: Node = None
        self.__length = 0

    def get_length(self):
        return self.__length

    def is_empty(self):
        return self.__top == None

    def peek(self):
        return self.__top.data

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.__top
        self.__top = new_node
        self.__length += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")

        data = self.__top.data
        old_top = self.__top
        self.top = self.__top.next
        old_top.next = None
        self.__length -= 1
        return data

    def display_all(self):
        current = self.__top
        while current != None:
            print(current.data)
            current = current.next


# Testing

class StackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()
    
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_push(self):
        self.stack.push(10)
        self.assertEqual(self.stack.get_length(), 1)
        self.assertEqual(self.stack.peek(), 10)

    def test_pop(self):
        self.stack.push(12)
        self.stack.push(13)
        self.stack.push(15)

        self.assertEqual(self.stack.get_length(), 3)
        data = self.stack.pop()
        self.assertEqual(data, 15) # first in last out
        self.assertEqual(self.stack.get_length(), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)



