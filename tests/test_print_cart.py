import io
import unittest
from contextlib import redirect_stdout

from aims.cart import Cart


class TestPrintCart(unittest.TestCase):
    def test_print_empty_cart(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            Cart().print_cart()
        self.assertIn("The cart is empty", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
