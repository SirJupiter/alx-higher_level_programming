#!/usr/bin/python3
"""script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

from sys import argv
import requests


def main():
    """Main function"""

    url = 'http://0.0.0.0:5000/search_user'

    q = ""
    if len(argv) == 2:
        q = argv[1]

    response = requests.post(url=url, data={'q': q})

    response_type = response.headers.get('Content-Type')

    if response_type == 'application/json':
        res = response.json()
        if res and res.get('id') and res.get('name'):
            print(f'[{res.id}] {res.name}')
        else:
            print('No result')
    else:
        print('Not a valid JSON')


if __name__ == "__main__":
    main()
