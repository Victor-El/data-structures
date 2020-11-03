import unittest

from structures.linked_list import LinkedList, IndexOutOfBoundException


class LinkedListTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    @staticmethod
    def class_started():
        print("LinkedListTestCase started")

    @staticmethod
    def class_finished():
        print("LinkedListTestCase finished")

    @classmethod
    def setUpClass(cls) -> None:
        cls.class_started()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.class_finished()

    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def tearDown(self) -> None:
        del self.linked_list

    def test_linked_list_count(self):
        self.linked_list.add(5)
        self.linked_list.add(4)
        self.linked_list.add(3)
        self.linked_list.add(2)
        self.linked_list.add(1)
        self.linked_list.add(0)

        self.assertEqual(6, self.linked_list.count, "list count = 6")

    def test_linked_list_add_and_get(self):
        self.linked_list.add(0)
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)

        self.assertEqual(0, self.linked_list.get(0))
        self.assertEqual(1, self.linked_list.get(1))
        self.assertEqual(2, self.linked_list.get(2))
        self.assertEqual(3, self.linked_list.get(3))

    def test_linked_list_remove(self):
        self.linked_list.add("vic")
        self.linked_list.add("chi")
        self.linked_list.add("ele")

        self.linked_list.remove(0)

        self.assertEqual("chi", self.linked_list.get(0))
        self.assertNotEqual(3, self.linked_list.count)
        self.assertEqual(2, self.linked_list.count)

        self.linked_list.remove(1)

        self.assertEqual("chi", self.linked_list.get(0), "LinkedList.remove(): should return chi")

    def test_linked_list_insert_at(self):
        self.linked_list.add(4)
        self.linked_list.add(2)
        self.linked_list.add(8)

        self.linked_list.insert_at(10, 1)

        self.assertEqual(10, self.linked_list.get(1))
        self.assertEqual(4, self.linked_list.count)

    def test_linked_list_add_first(self):
        self.linked_list.add(2)
        self.linked_list.add(4)
        self.linked_list.add(6)

        self.linked_list.add_first(10)

        self.assertEqual(4, self.linked_list.count, msg="count should be 4")
        self.assertEqual(10, self.linked_list.get(0), msg="10 should be first")

    def test_linked_list_add_last(self):
        self.linked_list.add(2)
        self.linked_list.add(4)
        self.linked_list.add(6)

        self.linked_list.add_last(10)

        self.assertEqual(10, self.linked_list.get(3), "LinkedList.add_last(). Last element should be 10")
        self.assertEqual(4, self.linked_list.count, "LinkedList.add_last(). List size should be 4")

    def test_linked_list_get_first(self):
        self.linked_list.add(2)
        self.linked_list.add(4)
        self.linked_list.add(6)

        self.assertEqual(2, self.linked_list.get_first(), "LinkedList.get_first(): first element of list")

    def test_linked_list_get_last(self):
        self.linked_list.add(2)
        self.linked_list.add(4)
        self.linked_list.add(6)

        self.assertEqual(6, self.linked_list.get_last(), "LinkedList.get_last(): last element of list")

    def test_linked_list_remove_first(self):
        self.linked_list.add(2)
        self.linked_list.add(8)
        self.linked_list.add(3)
        self.linked_list.add(2)
        self.linked_list.add(7)
        self.linked_list.add(0)
        self.linked_list.add(5)

        initial_count = self.linked_list.count

        self.linked_list.remove_first()

        msg = "LinkedList.remove_first(). current count should equal initial count - 1"
        self.assertEqual(initial_count - 1, self.linked_list.count, msg)
        self.assertEqual(8, self.linked_list.get(0), "LinkedList.remove_first(). first element should now be 8")

    def test_linked_list_remove_last(self):
        self.linked_list.add(1)
        self.linked_list.add(8)
        self.linked_list.add(3)
        self.linked_list.add(2)
        self.linked_list.add(7)
        self.linked_list.add(0)
        self.linked_list.add(5)

        initial_count = self.linked_list.count

        self.linked_list.remove_last()

        msg = "LinkedList.remove_last(). current count should equal initial count - 1"
        self.assertEqual(initial_count - 1, self.linked_list.count, msg)
        self.assertEqual(0, self.linked_list.get(self.linked_list.count - 1), "LinkedList.remove_last(). last "
                                                                              "element should now be 0")

    def test_linked_list_clear(self):
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)
        self.linked_list.add(4)

        self.assertEqual(4, self.linked_list.count, "LinkedList.clear(): list should have 4 elements")

        self.linked_list.clear()

        self.assertRaises(IndexOutOfBoundException, self.linked_list.get, 0)
        self.assertEqual(0, self.linked_list.count, "LinkedList.clear(): list should be empty")

    def test_linkedList_search(self):
        self.linked_list.add(0)
        self.linked_list.add(1)
        self.linked_list.add(2)
        self.linked_list.add(3)

        self.assertEqual(1, self.linked_list.search(1), "LinkedList.search() should find 1 at index 1")

    def test_linked_list_sort(self):
        self.linked_list.add(4)
        self.linked_list.add(8)
        self.linked_list.add(3)
        self.linked_list.add(2)
        self.linked_list.add(7)
        self.linked_list.add(0)
        self.linked_list.add(5)

        self.linked_list.sort()

        self.assertEqual(7, self.linked_list.count, msg="sort count assertion")
        self.assertEqual(0, self.linked_list.get(0), msg="check sort first element")
        self.assertEqual(2, self.linked_list.get(1), msg="check sort second element")

    def test_linked_list_reverse(self):
        self.linked_list.add(9)
        self.linked_list.add(8)
        self.linked_list.add(7)

        self.linked_list.reverse()

        self.assertEqual(7, self.linked_list.get(0), "LinkedList.Reverse() test")


if __name__ == '__main__':
    unittest.main()
