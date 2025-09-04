import unittest
from task4 import ShoppingCart
class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_single_item(self):
        self.cart.add_item("apple", 1.50)
        self.assertEqual(self.cart.items, {"apple": [1.50]})
        self.assertAlmostEqual(self.cart.total_cost(), 1.50)

    def test_add_multiple_items(self):
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("banana", 2.00)
        self.cart.add_item("orange", 1.25)
        self.assertEqual(self.cart.items, {"apple": [1.50], "banana": [2.00], "orange": [1.25]})
        self.assertAlmostEqual(self.cart.total_cost(), 4.75)

    def test_add_same_item_multiple_times(self):
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("apple", 2.00)
        self.cart.add_item("apple", 1.25)
        self.assertEqual(self.cart.items, {"apple": [1.50, 2.00, 1.25]})
        self.assertAlmostEqual(self.cart.total_cost(), 4.75)

    def test_remove_item_once(self):
        self.cart.add_item("apple", 1.50)
        self.cart.add_item("apple", 2.00)
        self.cart.remove_item("apple")
        self.assertEqual(self.cart.items, {"apple": [1.50]})
        self.assertAlmostEqual(self.cart.total_cost(), 1.50)

    def test_remove_item_until_empty(self):
        self.cart.add_item("banana", 2.00)
        self.cart.add_item("banana", 3.00)
        self.cart.remove_item("banana")
        self.cart.remove_item("banana")
        self.assertNotIn("banana", self.cart.items)
        self.assertAlmostEqual(self.cart.total_cost(), 0.0)

    def test_remove_item_not_in_cart(self):
        self.cart.add_item("apple", 1.50)
        self.cart.remove_item("banana")  # Should do nothing
        self.assertEqual(self.cart.items, {"apple": [1.50]})
        self.assertAlmostEqual(self.cart.total_cost(), 1.50)

    def test_total_cost_empty_cart(self):
        self.assertAlmostEqual(self.cart.total_cost(), 0.0)

    def test_add_and_remove_various(self):
        self.cart.add_item("apple", 1.00)
        self.cart.add_item("banana", 2.00)
        self.cart.add_item("apple", 1.50)
        self.cart.remove_item("apple")
        self.assertEqual(self.cart.items, {"apple": [1.00], "banana": [2.00]})
        self.assertAlmostEqual(self.cart.total_cost(), 3.00)

    def test_remove_item_from_empty_cart(self):
        self.cart.remove_item("apple")  # Should not raise error
        self.assertEqual(self.cart.items, {})
        self.assertAlmostEqual(self.cart.total_cost(), 0.0)

    def test_add_item_with_float_price(self):
        self.cart.add_item("milk", 2.99)
        self.cart.add_item("bread", 1.49)
        self.assertAlmostEqual(self.cart.total_cost(), 4.48)

if __name__ == "__main__":
    unittest.main()
