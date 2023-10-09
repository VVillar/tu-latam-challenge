import unittest
from unittest.mock import patch
from send_post_request import send_post_request

class TestSendPostRequest(unittest.TestCase):

    @patch('send_post_request.requests.post')
    def test_send_post_request_success(self, mock_post):
        # Configure the mock to return a successful response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "Success"}

        # Define the test data
        api_url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/devops"
        data = {
            "name": "Victor Villar",
            "mail": "victor.villar@globant.com",
            "github_url": "https://github.com/VVillar/tu-latam-challenge.git"
        }

        # Call the function to be tested
        success, response_data = send_post_request(api_url, data)

        # Assertions
        self.assertTrue(success)
        self.assertEqual(response_data, {"message": "Success"})

    @patch('send_post_request.requests.post')
    def test_send_post_request_failure(self, mock_post):
        # Configure the mock to raise an exception
        mock_post.side_effect = Exception("Connection error")

        # Define the test data
        api_url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/devops"
        data = {
            "name": "Victor Villar",
            "mail": "victor.villar@globant.com",
            "github_url": "https://github.com/VVillar/tu-latam-challenge.git"
        }

        # Call the function to be tested
        success, response_data = send_post_request(api_url, data)

        # Assertions
        self.assertFalse(success)
        self.assertEqual(response_data, "Ocurrio un error: Connection error")

if __name__ == '__main__':
    unittest.main()
