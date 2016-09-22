import unittest
from fellowClass import Fellow


class TestFellow(unittest.TestCase):
    """

    This is Test class for Room class and its methods.
    It contains tests for the get_name, print_room,
    print_allocations and print_unallocated methods.

    """

    def setUp(self):
        self.test_fellow = Fellow()

    def test_class_initialization(self):
        self.assertIsInstance(
            self.test_fellow, Fellow, msg="Cannot create `Fellow` instance")
