from django.test import TestCase

# Create a django unit test class inheriting from the TestCase class
#

class Unit_Test(TestCase):

    # create a test for User
    def test_unit_test(self):
        # Assert that the test is working
        self.assertEqual(1, 1)

