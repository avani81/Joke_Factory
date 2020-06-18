""" Libraries for Jokes API requests and response schema """

import requests


class JokeAPI:
    """
    Jokes API defination class.
    """

    def __init__(self):
        self.base_url = 'https://official-joke-api.appspot.com/'
        self.client = requests

    def get_programing_jokes_random(self):
        """Test helper for GET jokes/programming/random."""
        url = self.base_url + 'jokes/programming/random'
        resp = self.client.request(method='GET', url=url)
        return resp

    def get_programing_jokes_ten(self):
        """Test helper for GET jokes/programming/ten."""
        url = self.base_url + 'jokes/programming/ten'
        resp = self.client.request(method='GET', url=url)
        return resp

    def get_random_jokes(self):
        """Test helper for GET jokes/random."""
        url = self.base_url + 'jokes/random'
        resp = self.client.request(method='GET', url=url)
        return resp

    def get_ten_jokes(self):
        """Test helper for GET jokes/ten."""
        url = self.base_url + '/jokes/ten'
        resp = self.client.request(method='GET', url=url)
        return resp


class ProgrammingJokesSchema:
    """Jokes API response defination."""
    programming_jokes_response = {
        "type": "array",
        "items": {
            "type": "object",
            "properties":   {
                "id": {"type": "number"},
                "type": {"type": "string"},
                "setup": {"type": "string"},
                "punchline": {"type": "string"}
                }
            }
        }
