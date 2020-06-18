import logging

from jsonschema import validate
from unittest import TestCase
from libs.joke_api import JokeAPI
from libs.joke_api import ProgrammingJokesSchema
from utils.custom_logger import CustomLogger


class ProgrammingJokesTests(TestCase):
    """
    This class includes GET API tests for /jokes and /jokes/programming/
    endpoints.
    """
    @classmethod
    def setUpClass(cls):
        cls.jokes_api = JokeAPI()
        cls.log = CustomLogger()
        
    def test_get_random_programing_jokes(self):
        """
        Test 1 - Validate GET /jokes/programming/random API
        Validation - Verify Response code 200 and type of joke programming
        Validate response schema for all fields - id,type,setup and punchline
        """
        resp = self.jokes_api.get_programing_jokes_random()
        self.assertEqual(200, resp.status_code, msg='response code not match')
        obj = resp.json()
        logging.debug('Response {0}'.format(obj))
        self.assertEqual('programming', obj[0]['type'], msg='Type not valid')
        validate(obj, schema=ProgrammingJokesSchema.programming_jokes_response)

    def test_get_ten_programing_jokes(self):
        """
        Test 2 - Validate GET /jokes/programming/ten API
        Validation - 1) Validate API Response code 200
        2) Validate that 10 jokes are returned
        3) Validate response schema for all fields - id ,type,setup & punchline
        4) Validate that all jokes are of type "programming"
        """
        resp = self.jokes_api.get_programing_jokes_ten()
        self.assertEqual(200, resp.status_code, msg='status code not match')
        obj = resp.json()
        logging.debug('Response {0}'.format(obj))
        logging.debug('Validate that 10 jokes are returned')
        self.assertEqual(10, len(obj), msg='list count does not match to 10')
        validate(obj, schema=ProgrammingJokesSchema.programming_jokes_response)
        logging.debug('Validate that all jokes are of type - programming')
        for i in range(10):
            self.assertEqual('programming', obj[i]['type'])

    def test_get_general_random_jokes(self):
        """
        Test-3 Validate GET /jokes/random endpoint.
        Validation - 1) Validate API Response code 200
        2) Validate that all jokes are of type "programming" or "general"
        """
        resp = self.jokes_api.get_random_jokes()
        self.assertEqual(200, resp.status_code, msg='response code not match')
        obj = resp.json()
        logging.debug('Response {0}'.format(obj))
        self.assertIn(obj['type'], ['general', 'programming'])

    def test_get_general_ten_jokes(self):
        """
        Test-4 Validate GET /jokes/ten endpoint.
        Validation - 1) Validate API Response code 200
        2) Validate response list schema for all fields.
        """
        resp = self.jokes_api.get_ten_jokes()
        self.assertEqual(200, resp.status_code, msg='response code not match')
        obj = resp.json()
        logging.debug('Response {0}'.format(obj))
        validate(obj, schema=ProgrammingJokesSchema.programming_jokes_response)
