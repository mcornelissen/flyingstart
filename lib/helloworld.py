""" Print Hello world

    Usage:

        python helloworld.py
"""
import unittest 

def hi():
    """ Print Hello world """
    print("hello world")


class HelloWorldTest(unittest.TestCase):

    def test_function_runs(self):
        hi()


if __name__ == '__main__':
    unittest.main()

