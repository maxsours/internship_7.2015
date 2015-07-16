import unittest
from ..number import app


class TestOperate(unittest.TestCase):
    """
    Test the operate function
    """
    def test_add(self):
        with app.app_context():
            resp = app.test_client().get('/4/2/?operation=addition')
            self.assertEqual(resp.data, "6")
            
    def test_subtract(self):
        with app.app_context():
            resp = app.test_client().get('/4/2/?operation=subtraction')
            self.assertEqual(resp.data, "2")
            
    def test_multiply(self):
        with app.app_context():
            resp = app.test_client().get('/4/2/?operation=multiplication')
            self.assertEqual(resp.data, "8")
            
    def test_divide(self):
        with app.app_context():
            resp = app.test_client().get('/4/2/?operation=division')
            self.assertEqual(resp.data, "2")
