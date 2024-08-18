import unittest

import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print("this is a set up function")
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        '''just random command'''
        test_param = 'Hey'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_lower(self):
        test_param = None
        result = main.lower(test_param)
        self.assertEqual(result, "please enter a number")

    def test_lower1(self):
        test_param = ''
        result = main.lower(test_param)
        self.assertEqual(result, "please enter a number")

    def test_low2(self):
        test_param = 0
        result = main.lower(test_param)
        self.assertEqual(result, "please enter a number")

    def test_adder(self):
        test_param = 10
        test_param2 = 10
        result = main.adder(test_param, test_param2)
        self.assertEqual(result, 20)

    def tearDown(self):
        print("run end of each test")


if __name__ == "__main__":
    unittest.main()
