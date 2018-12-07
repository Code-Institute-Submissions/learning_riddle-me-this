import requests
import run
import unittest

# TODO
# TOREVIEW 
# should we use index function??
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
        html_txt = requests.get(url, headers=headers).text
        self.assertIn(btn_element, html_txt)


    def test_indexhtml_post(self):
        """
        Returns the username when POST request
        """
        url = 'https://riddle-me-this-joseppujol.c9users.io/'
        usrname = 'theUser'
        headers = {'Connection':'close'}
        html_txt = requests.get(url + usrname, headers=headers).text
        self.assertIn(usrname, html_txt)
    
    
    def test_add_usernames_only_unique(self):
        """
        Usernames added correctly and are unique
        """
        url = 'https://riddle-me-this-joseppujol.c9users.io/'
        usrnames_test = ['usr1', 'usr2', 'usr3', 'usr1']
        unique_usrnames = ['usr1', 'usr2', 'usr3',]
        headers = {'user-agent': 'Headless', 
                   'origin': 'http://riddle-me-this-joseppujol.c9users.io',
                   'Connection':'close'}
        cookies = {'c9.live.user.click-through': 'ok'}
        
        for user in usrnames_test:
            data = {'username': user}
            r = requests.post(url, data=data,
                              headers=headers, 
                              cookies=cookies)
        html_txt = requests.get(url + 'print_users', 
                                headers=headers).text
        usrnames_html = [itm for itm in html_txt.split(' ') if itm != '']
        self.assertEqual(usrnames_html, unique_usrnames)
    
    
    def test_riddlehtml_get(self):
        """
        Renders riddle.html when GET request 
        """
        url = 'https://riddle-me-this-joseppujol.c9users.io/riddle'
        btn_element = "<button>Submit!</button>"
        headers = {'Connection':'close'}
        html_txt = requests.get(url, headers=headers).text
        self.assertIn(btn_element, html_txt)    
