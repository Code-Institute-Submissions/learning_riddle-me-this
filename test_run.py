import requests
import run
import unittest

# TODO
# TO BE REVIEWED. should we use index function??
# is it ok to have variables in a test function?

class TestRun(unittest.TestCase):
    """
    Our test suite for riddle-me-this, run.py file
    """
    def test_indexhtml_get(self):
        """
        Renders index.html when GET request 
        """
        url = 'https://riddle-me-this-joseppujol.c9users.io/'
        btn_element = "<button>Let's riddle!</button>"
        headers = {'Connection':'close'}
        html_text = requests.get(url, headers=headers).text
        self.assertIn(btn_element, html_text)

    def test_indexhtml_post(self):
        """
        Returns the username when POST request
        """
        url = 'https://riddle-me-this-joseppujol.c9users.io/'
        username = 'theUser'
        headers = {'Connection':'close'}
        
        r = requests.get(url + username, headers=headers)
        html_text = r.text
        self.assertIn(username, html_text)
    
    def test_add_usernames_only_unique(self):
        """
        Usernames added correctly in temporary variable run.usernames
        """
        url = 'https://riddle-me-this-joseppujol.c9users.io/'
        usrnames_test = ['username1', 'username2', 'username3', 'username1']
        unique_usrnames = ['username1', 'username2', 'username3',]
        headers = {'user-agent': 'Headless', 
                   'origin': 'http://riddle-me-this-joseppujol.c9users.io',
                   'Connection':'close'}
        cookies = {'c9.live.user.click-through': 'ok'}
        
        for user in usrnames_test:
            data = {'username': user}
            r = requests.post(url, data=data,
                              headers=headers, 
                              cookies=cookies)
        html_text = requests.get(url + 'print_usernames', 
                                 headers=headers).text
        usrnames_html = [item for item in html_text.split(' ') if item != '']
        self.assertEqual(usrnames_html, unique_usrnames)
    
    
