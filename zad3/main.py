import requests
import json
import unittest
import re
import tqdm

class MainUnitTests(unittest.TestCase):

    tqdm_bar = tqdm.tqdm(total=7, unit='tests', position=0, leave=False, colour='green')

    # Check if the response is 200
    def test_status_code_is_200(self):
        req = requests.get('https://passwordinator.herokuapp.com/generate')
        status = req.status_code
        self.assertEqual(status, 200)
        self.tqdm_bar.update(1)

    # Check if generated password has a number
    def test_pass_has_number(self):
        req = requests.get('https://passwordinator.herokuapp.com/generate?num=true')
        js = json.loads(req.text)
        self.assertTrue(re.search(r'\d', js['data']))
        self.tqdm_bar.update(1)

    # Check if generated password is longer than 5 characters
    def test_pass_is_5_char_long(self):
        req = requests.get('https://passwordinator.herokuapp.com/generate?len=5')
        js = json.loads(req.text)
        self.assertEqual(len(js['data']), 5)
        self.tqdm_bar.update(1)

    # Check if providing no arguments returns a random password
    def test_default_pass_generated(self):
        req = requests.get('https://passwordinator.herokuapp.com/generate')
        js = json.loads(req.text)
        self.assertEqual(len(js['data']) > 0, True)
        self.tqdm_bar.update(1)

    # Check if password has capslock in it
    def test_pass_has_capslock(self):
        req = requests.get('https://passwordinator.herokuapp.com/generate?caps=true')
        js = json.loads(req.text)
        self.assertEqual(bool(re.match(r'\w*[A-Z]\w*', js['data'])), True)
        self.tqdm_bar.update(1)

    # Check if password has special characters
    def test_pass_has_special_char(self):
        req = requests.get('https://passwordinator.herokuapp.com/generate?char=true')
        js = json.loads(req.text)
        self.assertEqual(any(not c.isalnum() for c in js['data']), True)
        self.tqdm_bar.update(1)

    # Check if wrong arguments throw an error
    def test_pass_wrong_arguments(self):
        req = requests.get('https://passwordinator.herokuapp.com/generate?len=asdasdsasa')
        js = json.loads(req.text)
        self.assertEqual(js['data'], '')
        self.tqdm_bar.update(1)

