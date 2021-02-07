import unittest
import average_of_elements_in_a_list

class TestCase(unittest.TestCase):
    
    #testing list sizeof 4
    def test_list_size_4(self):
        list = {1, 1, 2, 2} #answer key: average = 1.5
        self.assertEqual(average_of_elements_in_a_list.average_of_list(list), 1.5)

    #testing list sizeof 1
    def test_list_size_1(self):
        list = {1} #answer key: average = 1
        self.assertEqual(average_of_elements_in_a_list.average_of_list(list), 1)

    #testing list sizeof 0
    def test_list_size_0(self):
        list = {} #answer key: average = DNE
        self.assertEqual(average_of_elements_in_a_list.average_of_list(list), 0)



if __name__ == '__main__':
    unittest.main(verbosity=2)