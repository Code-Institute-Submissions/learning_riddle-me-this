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
        btn_element = "</button>"
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
        url = 'https://riddle-me-this-joseppujol.c9users.io/usr1/1'
        btn_element = "</button>"
        headers = {'Connection':'close'}
        html_txt = requests.get(url, headers=headers).text
        self.assertIn(btn_element, html_txt)    


    def test_read_riddlesjson(self):
        """
        read_riddles function reads riddles correctly
        """
        riddles_to_test = [
             {'riddle_id': '5',
              'riddle': 'What is so delicate that saying its name breaks it?',
              'answer': 'Silence'},
             {'riddle_id': '10',
              'riddle': 'Which word in the dictionary is spelled incorrectly?',
              'answer': 'Incorrectly'},]
        riddles_function = run.read_riddlesjson()
        for riddle in riddles_function:
            if riddle['riddle_id'] == '5':
                self.assertEqual(riddle['riddle'], riddles_to_test[0]['riddle'])
            if riddle['riddle_id'] == '10':
                self.assertEqual(riddle['riddle'], riddles_to_test[1]['riddle'])


    def test_next_riddle(self):
        """
        test get_riddle function yields riddles
        """
        riddles = run.read_riddlesjson()
        for i in range(0, 5):
            riddl = run.next_riddle(riddles)
        self.assertEqual(riddl['riddle_id'], '5')
        for j in range(0, 3):
            riddl = run.next_riddle(riddles)
        self.assertEqual(riddl['riddle_id'], '8')
        
            