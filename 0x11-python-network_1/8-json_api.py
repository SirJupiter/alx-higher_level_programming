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

    try:
        res = response.json()
        if res == {}:
            print("No result")
        else:
            print(f"[{res.get('id')}] {res.get('name')}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
