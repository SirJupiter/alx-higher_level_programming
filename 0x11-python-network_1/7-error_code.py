#!/usr/bin/python3
"""script takes in a URL, sends a request to the URL
and displays the body of the response.
"""

from sys import argv
import requests


def main():
    """Main function"""

    url = argv[1]

    try:
        res = requests.get(url=url)
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.status_code >= 400:
            print(f'Error code: {e.status_code}')
        else:
            pass


if __name__ == "__main__":
    main()
