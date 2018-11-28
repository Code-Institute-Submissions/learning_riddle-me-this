import run
import unittest

# Hello world test
class test_run(unittest.TestCase):
    def test_is_this_thing_on(self):
        self.assertEqual(1, 1)


class TestRun(unittest.TestCase):
    '''
    Our test suite for riddle-me-this, run.py file
    '''
    
    