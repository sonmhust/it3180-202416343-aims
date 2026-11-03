import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearchByTitle(unittest.TestCase):
    def test_case_insensitive(self):
        items = [DigitalVideoDisc("The Lion King")]
        self.assertEqual(len(search_by_title(items, "lion")), 1)


if __name__ == "__main__":
    unittest.main()
