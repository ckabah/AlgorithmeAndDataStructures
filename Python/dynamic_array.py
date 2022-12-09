import  unittest


class DynamicArray:
    """
    This is a basic implementation of Dynamic Array.
    In doc, d_array => Dynamic Array.

    """
    def __init__(self, capacity=1):
        self._size = 0 # Empty d_array have size 0.
        self._capacity = capacity # 1 by default
        self._array = [None]*self._capacity 

    def get_item(self, idex):
        """
        Retreive element at index idex if it exist and return its value.

        Parameters
        ----------
        idex : int
            It index (position) of element to retreive.
        
        Returns
        -------
        Any:
            Value of element at index idex.

        """
        if idex >= self._size:
            raise IndexError('This is too large')
    
        return self._array[idex]

    def get_len(self):
        """ Return last size  for d_array """
        return self._size
    
    def get_capacity(self):
        """ Return last capacity  for d_array"""
        return self._capacity
    
    def __resize(self, new_capacity):
        """
        Create a new array with size new_capacity and copy last array in.
        It's used to reize d_array is append fonction (if size==capacity),
        pop and remove_at (if size < capacity//4)
        
        Parameters
        ----------
        new_capacity : int
            This new_capacity will be new capacity of d_array
        """
        new_array = [None]*new_capacity
        for i in range(0, self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def append(self, data):
        """
        Add element in last position.

        Parameters
        ----------
        data : Any
        """
        if self._size==self._capacity:
            self.__resize(2*self._capacity)
        self._array[self._size] = data
        self._size +=1
    
    def pop(self):
        """
        Delete last element if array is not empty in return its value.
        
        Returns
        -------
        Any
            None if d_array is empty
            data if d_array not empty
        """
        if self._size >=1:
            data = self._array[self._size -1]
            self._array[self._size -1] = None
            self._size -=1
            if self._size < self._capacity //4:
                self.__resize(self._capacity//2)
            return data
        return None

    def remove_at(self, idex):
        """
        Delete element at index idex  if d_array is not empty.

        Parameters
        ----------
        index : int
        """
        if idex >= self._size:
            raise IndexError('This index is too large')
        
        for i in range(self._size):
            if i == idex:
                for j in range(i, self._size):
                    self._array[j] = self._array[j+1]
                self._array[self._size -1] = None
                self._size -=1
                if self._size < self._capacity //4:
                    self.__resize(self._capacity//2)
                break

    def display(self):
        """ Print all element in d_array."""
        for i in range(self._size):
            print(self._array[i])

    def is_empty(self):
        """ Check if d_array is empty or no."""
        return True if self._size==0 else False
    
    def clear(self):
        """Reunitialize the d_array."""
        self._size = 0
        self._capacity = 1
        self._array = [None]*self._capacity


# Unit Testing

class DynamicArrayTestCase(unittest.TestCase):
    
    def setUp(self):
         self.dynamic_array = DynamicArray()
    
    def test_append(self):
        self.assertTrue(callable(self.dynamic_array.append))
        self.assertTrue(self.dynamic_array.is_empty())
        self.dynamic_array.append(10)
        self.assertFalse(self.dynamic_array.is_empty())
        self.assertEqual(self.dynamic_array.get_item(0), 10)
        self.assertRaises(IndexError, self.dynamic_array.get_item, 2)
    
    def test_get_item(self):
        self.dynamic_array.append(22)
        self.dynamic_array.append(58)
        self.dynamic_array.append(66)
        self.assertEqual(self.dynamic_array.get_item(1), 58)

    def test_pop(self):
        for i in range(10):
            self.dynamic_array.append(i*2 - i + 1)
        size = self.dynamic_array.get_len()
        last_item = self.dynamic_array.get_item(size - 1)
        self.assertEqual(size, 10)
        item = self.dynamic_array.pop()
        self.assertEqual(item,  last_item)
        self.assertEqual(self.dynamic_array.get_len(), 9)

    def test_remove_at(self):
        for i in range(10):
            self.dynamic_array.append(i*2 - i + 1)
        size = self.dynamic_array.get_len()
        self.assertEqual(size, 10)
        self.dynamic_array.remove_at(5)
        size = self.dynamic_array.get_len()
        self.assertEqual(size, 9)

if __name__ == "__main__":
    unittest.main(verbosity=2)
    