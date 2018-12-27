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
        form_id = 'id="username"'
        headers = {'Connection':'close'}
        html_txt = requests.get(url, headers=headers).text
        self.assertIn(form_id, html_txt)


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
        headers = {'Connection':'close'}
        usr = 'usr1'
        riddle_id = '1'
        form_id = 'id="answer"'
        url_page = url + '/' + usr + '/' + riddle_id
        html_txt = requests.get(url_page, headers=headers).text
        self.assertIn(form_id, html_txt)    


    def test_read_riddlesjson(self):
        """
        read_riddles function reads riddles correctly
        """
        riddles_to_test = {
            '5': {
              'question': 'What is so delicate that saying its name breaks it?',
              'answer': 'Silence'},
            '10': {
              'question': 'Which word in the dictionary is spelled incorrectly?',
              'answer': 'Incorrectly'}}
        riddles = run.read_riddlesjson()
        for riddle in riddles:
            if riddle == '5':
                self.assertEqual(riddles[riddle]['question'], 
                                 riddles_to_test['5']['question'])
            if riddle == '10':
                self.assertEqual(riddles[riddle]['question'], 
                                 riddles_to_test['10']['question'])
    
    
    def test_riddles_completed(self):
        """
        Message informs users when all riddles are completed 
        """
        riddles = run.read_riddlesjson()
        riddle_id = str(len(riddles) + 1)
        
        msg = "You did all riddles"
        url = 'https://riddle-me-this-joseppujol.c9users.io/riddle'
        usr = 'usr1'
        headers = {'user-agent': 'Headless', 
                   'origin': 'http://riddle-me-this-joseppujol.c9users.io',
                   'Connection':'close'}
        cookies = {'c9.live.user.click-through': 'ok'}
        
        url_page = url + '/' + usr + '/' + riddle_id
        html_txt = requests.get(url_page, headers=headers).text
        self.assertIn(msg, html_txt)


    def test_leaderboardhtml_get(self):
        """
        Renders index.html when GET request 
        """
        url = 'https://riddle-me-this-joseppujol.c9users.io/leaderboard'
        form_id = 'leaderboard' #'id="username"'
        headers = {'Connection':'close'}
        html_txt = requests.get(url, headers=headers).text
        self.assertIn(form_id, html_txt)
        

    # def test_next_riddle(self):
    #     """
    #     test get_riddle function yields riddles
    #     """
    #     for _ in range(0, 5):
    #         riddl, riddl_id = run.next_riddle()
    #     self.assertEqual(riddl['riddle_id'], '6')
    #     for _ in range(0, 3):
    #         riddl, riddl_id = run.next_riddle()
    #     self.assertEqual(riddl['riddle_id'], '9')


