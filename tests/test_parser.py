import unittest
from .. import parser


class TestParser(unittest.TestCase):
    """
    Test the Parser module
    """
    def test_get_random_number_from_website(self):
        """
        the function should return an integer random number from the website
        """
        result, resp = parser.get_random_number_from_website(min=1, max=3)
        self.assertEqual(resp.status_code, 200)
        self.assertLessEqual(result, 3)
        self.assertGreaterEqual(result, 1)



