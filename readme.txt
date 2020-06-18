This project includes test Libraries and tests for Joke Factory APIs

Tests include following endpoints validation ( functional tests only)
Using https://official-joke-api.appspot.com/jokes/programming/random
Validate that the returned Joke is of type "programming"

Using https://official-joke-api.appspot.com/jokes/programming/ten
Validate that 10 jokes are returned
Validate that all jokes are of type "programming"

Additional tests for validation for following endpoints for general type
https://official-joke-api.appspot.com/jokes/ten
https://official-joke-api.appspot.com/jokes/random

Requirements
python3
jsonschema

File Structure
chime_programming_jokes/libs
chime_programming_jokes/tests

Usage
Command -  python3 -m unittest tests/programming_jokes_tests.py -v

Example Results
home$ python3 -m unittest tests/programming_jokes_tests.py -v
test_get_general_random_jokes (tests.programming_jokes_tests.ProgrammingJokesTests) ... ok
test_get_general_ten_jokes (tests.programming_jokes_tests.ProgrammingJokesTests) ... ok
test_get_random_programing_jokes (tests.programming_jokes_tests.ProgrammingJokesTests) ... ok
test_get_ten_programing_jokes (tests.programming_jokes_tests.ProgrammingJokesTests) ... ok

----------------------------------------------------------------------
Ran 4 tests in 1.795s

OK
