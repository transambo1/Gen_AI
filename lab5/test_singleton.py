import unittest
from singleton import A

class TestSingleton(unittest.TestCase):
    def test_singleton_should_return_same_instance(self):
        # Khởi tạo 2 biến từ cùng 1 class A
        a1 = A()
        a2 = A()

        # Kiểm tra xem a1 và a2 có trỏ về cùng một vùng nhớ (cùng 1 instance) hay không
        self.assertIs(a1, a2)

if __name__ == "__main__":
    unittest.main()