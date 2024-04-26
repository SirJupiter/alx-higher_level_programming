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
        status_code = res.status_code
    except requests.exceptions.RequestException as _:
        if status_code >= 400:
            print(f'Error code: {status_code}')
        else:
            pass


if __name__ == "__main__":
    main()
