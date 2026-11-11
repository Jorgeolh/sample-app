import unittest
import requests

class TestSampleApp(unittest.TestCase):
    def test_page(self):
        url = "http://172.17.0.1:5050/"
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()
