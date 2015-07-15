import unittest
from ..number import app


class TestOperate(unittest.TestCase):
    """
    Test the operate function
    """
    def test_add(self):
        with app.app_context():
            resp = app.test_client().get('/3/4/?operation=addition')
            self.assertEqual(resp.data, "7")
