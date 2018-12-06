import logging
import requests
import run
import unittest


class TestRun(unittest.TestCase):
    '''
    Our test suite for riddle-me-this, run.py file
    '''
    # TO BE REVIEWED. should we use index function??
    def test_indexhtml_get(self):
        '''
        Loads the index.html when we call index() with GET request 
        '''
        url = 'https://riddle-me-this-joseppujol.c9users.io/'
        btn_element = "<button>Let's riddle!</button>"
        headers = {'Connection':'close'}
        html_text = requests.get(url, headers=headers).text
        # Button element in HTML?
        self.assertIn(btn_element, html_text)

    # TO BE REVIEWED. should we use index function??
    # is it ok to have variables in a test function?
    def test_indexhtml_post(self):
        '''
        Returns the username in the html call index() with POST request
        '''
        url = 'https://riddle-me-this-joseppujol.c9users.io/'
        username = 'theUser'
        headers = {'Connection':'close'}
        r = requests.get(url + username, headers=headers)
        html_text = r.text
        # Username in HTML?
        self.assertIn(html_text, html_text)
    

        