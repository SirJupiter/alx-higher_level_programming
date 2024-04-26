#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and displays the value of the variable X-Request-Id
in the response header
"""

import requests
from sys import argv


def main():
    """Main function"""

    url = argv[1]

    req = requests.get(url=url)
    response = req.headers.get('X-Request-Id')

    print(response)


if __name__ == "__main__":
    main()
