import unittest
import requests
import json

class TestCognianceApi(unittest.TestCase):

    def test_get_candidates(self):
        r = requests.get('http://qainterview.cogniance.com/candidates', auth=('', ''))
        self.assertEqual(r.status_code, 200)

    # To get one we need get valid id first, so we need to use parsing
    def test_get_one_candidate(self):
        r = requests.get('http://qainterview.cogniance.com/candidates', auth=('', ''))
        candidate = json.loads(r.text)
        id = candidate["candidates"][0]["id"]
        r = requests.get('http://qainterview.cogniance.com/candidates/' + str(id), auth=('', ''))
        self.assertEqual(r.status_code, 200)

    # In this method we are verifying response code and that all data is added correctly  
    def test_post_candidates_correct(self):
        url = 'http://qainterview.cogniance.com/candidates'
        candidate = {"name": "Vitiska Ekaterina","position": "QA"}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=candidate)
        self.assertEqual(r.status_code, 201)
        # Parsing response and comparing data
        candidate = json.loads(r.text)
        self.assertEqual(candidate["candidate"]["position"], "QA")
        self.assertEqual(candidate["candidate"]["name"], "Vitiska Ekaterina")
        id = candidate["candidate"]["id"]
        print("Candidate №" + str(id) + " was added during this test!")

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

    # Before deleting we must get valid id to delete, so we need to use parsing first
    def test_delete_candidates(self):
        r = requests.get('http://qainterview.cogniance.com/candidates', auth=('', ''))
        candidate = json.loads(r.text)
        id = candidate["candidates"][0]["id"]
        print("Candidate №" + str(id) + " will be deleted during this test!")
        r = requests.delete('http://qainterview.cogniance.com/candidates/'+ str(id), auth=('', ''))
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
input()
