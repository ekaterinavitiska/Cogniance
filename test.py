import unittest
import requests
import json

class TestCognianceApi(unittest.TestCase):

    def test_get_candidates(self):
        r = requests.get('http://qainterview.cogniance.com/candidates', auth=('', ''))
        self.assertEqual(r.status_code, 200)

    def test_get_one_candidate(self):
        r = requests.get('http://qainterview.cogniance.com/candidates/1', auth=('', ''))
        self.assertEqual(r.status_code, 200)
      
    def test_post_candidates_correct(self):
        url = 'http://qainterview.cogniance.com/candidates'
        candidate = {"name": "Vitiska Ekaterina","position": "QA"}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=candidate)
        self.assertEqual(r.status_code, 201)

    # In this test we skipped header Content-Type, method should return Status 400
    # This method works incorrect according documentation
    def test_post_candidates_incorr1(self):
        url = 'http://qainterview.cogniance.com/candidates'
        candidate = {"name": "Vitiska Ekaterina","position": "QA"}
        r = requests.post(url, json=candidate)
        self.assertEqual(r.status_code, 400)

    # In this test we skipped Name, method should return Status 400  
    def test_post_candidates_incorr2(self):
        url = 'http://qainterview.cogniance.com/candidates'
        candidate = {"position": "QA"}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=candidate)
        self.assertEqual(r.status_code, 400)

    def test_delete_candidates(self):
        r = requests.delete('http://qainterview.cogniance.com/candidates/1', auth=('', ''))
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
input()
