import unittest
from user import User

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Runs before all the tests
        print("setUpClass\n")

    @classmethod
    def tearDownClass(cls):
        # Runs after all the tests
        print("\ntearDownClass")

    def setUp(self):
        # setUp runs before every single test
        print("\nsetUp")
        self.user_1 = User("Andres", "Lopez")
        self.user_2 = User("Isabel", "Martinez")

    def tearDown(self):
        # Runs after every single test
        print("tearDown\n")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.user_1.email, "andres_lopez@email.com")
        self.assertEqual(self.user_2.email, "isabel_martinez@email.com")
        self.user_1.first_name = "AnDrew"
        self.user_1.last_name = "Esquivel"
        self.user_2.first_name = "cHabEla"
        self.user_2.last_name = "sAnchez"
        self.assertEqual(self.user_1.email, "andrew_esquivel@email.com")
        self.assertEqual(self.user_2.email, "chabela_sanchez@email.com")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.user_1.full_name, "Andres Lopez")
        self.assertEqual(self.user_2.full_name, "Isabel Martinez")
        self.user_1.first_name = "Andrew"
        self.user_1.last_name = "Esquivel"
        self.user_2.first_name = "Chabela"
        self.user_2.last_name = "Sanchez"
        self.assertEqual(self.user_1.full_name, "Andrew Esquivel")
        self.assertEqual(self.user_2.full_name, "Chabela Sanchez")

if __name__ == "__main__":
    unittest.main()
