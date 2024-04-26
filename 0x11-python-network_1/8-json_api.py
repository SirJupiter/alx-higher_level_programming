#!/usr/bin/python3
"""script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

from sys import argv
import requests


def Main():
    """Main function"""

    url = 'http://0.0.0.0:5000/search_user'

    q = ""
    if len(argv) == 2:
        q = argv[1]

    response = requests.post(url=url, data={'q': q})

    if response.status_code == 204:
        print('No result')
    elif response.status_code == 200:
        json_response = response.json()
        print(f'[{json_response[0]["id"]}] {json_response[0]["name"]}')
    else:
        print('Not a valid JSON')


if __name__ == "__main__":
    Main()
