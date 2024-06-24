import unittest
from src.logapp.auth import login
from src.logapp.database import add_user, setup_database

class TestLoginApp(unittest.TestCase):
    def setUp(self):
        setup_database()
        add_user('testuser', 'testpass', 'user')

    def test_login_success(self):
        success, message = login('testuser', 'testpass')
        self.assertTrue(success)
        self.assertEqual(message, "Welcome, testuser!")

    def test_login_failure(self):
        success, message = login('testuser', 'wrongpass')
        self.assertFalse(success)
        self.assertEqual(message, "Invalid username or password.")

if __name__ == '__main__':
    unittest.main()
